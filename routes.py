from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from extensions import db
from model import User
import http.client
import json

main = Blueprint('main', __name__)

def authenticate_with_angelone(client_id, pin, totp, api_key):
    """Helper function to authenticate with AngelOne API"""
    conn = http.client.HTTPSConnection("apiconnect.angelone.in")
    
    payload = json.dumps({
        "clientcode": client_id,
        "password": pin,
        "totp": totp,
        "state": "STATE_VARIABLE"
    })

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-UserType": "USER",
        "X-SourceID": "WEB",
        "X-ClientLocalIP": "CLIENT_LOCAL_IP",
        "X-ClientPublicIP": "CLIENT_PUBLIC_IP",
        "X-MACAddress": "MAC_ADDRESS",
        "X-PrivateKey": api_key
    }

    try:
        conn.request("POST", "/rest/auth/angelbroking/user/v1/loginByPassword", payload, headers)
        res = conn.getresponse()
        data = res.read()
        response_json = json.loads(data.decode("utf-8"))
        
        if response_json.get("status") and response_json.get("data", {}).get("jwtToken"):
            return response_json["data"]["jwtToken"]
        return None
    except Exception as e:
        print(f"Authentication error: {e}")
        return None

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        client_id = request.form['client_id']
        api_key = request.form['api_key']

        if User.query.filter_by(client_id=client_id).first():
            flash('Client ID already registered!', 'danger')
            return redirect(url_for('main.register'))

        new_user = User(username=username, client_id=client_id, api_key=api_key)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('main.login'))

    return render_template('register.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        client_id = request.form['client_id']
        pin = request.form['pin']
        totp = request.form['totp']

        user = User.query.filter_by(client_id=client_id).first()
        if not user:
            flash('Invalid Client ID!', 'danger')
            return redirect(url_for('main.login'))

        access_token = authenticate_with_angelone(client_id, pin, totp, user.api_key)
        if access_token:
            session['access_token'] = access_token
            session['client_id'] = client_id
            flash('Login successful!', 'success')
            return redirect(url_for('main.dashboard'))
        
        flash('Authentication failed!', 'danger')
        return redirect(url_for('main.login'))

    return render_template('login.html')

@main.route('/dashboard')
def dashboard():
    if 'access_token' not in session:
        flash('Please login to access the dashboard.', 'warning')
        return redirect(url_for('main.login'))
    return render_template('dashboard.html', username=session.get('client_id'))

@main.route('/logout')
def logout():
    session.clear()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('main.login'))
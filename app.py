from flask import Flask, render_template

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html', title="Open Terminal", slogan="Empowering Traders with Insight and Simplicity")

# About route
@app.route('/about')
def about():
    return render_template('about.html', title="About - Open Terminal", description="Open Terminal is a trading terminal for traders, built using Python, Flask, and AngelOne Smart API. It's designed for simplicity and efficiency.")

if __name__ == '__main__':
    app.run(debug=True)
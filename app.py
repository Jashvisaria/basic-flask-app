from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Home route (GET request)
@app.route('/')
def home():
    return render_template('index.html', title="Open Terminal", slogan="Empowering Traders with Insight and Simplicity")

# Form route (GET request)
@app.route('/form')
def form():
    return render_template('form.html', title="Trading Form")

# Example POST route for form submission
@app.route('/example-post', methods=['POST'])
def example_post():
    data = request.get_json()
    symbol = data.get('symbol')
    quantity = data.get('quantity')
    exchange = data.get('exchange')
    action = data.get('action')  # Capture whether it's 'buy' or 'sell'

    # Construct the response message
    if action == 'buy':
        response_message = f"Order received for {quantity} units of {symbol} on {exchange} exchange to BUY."
    else:
        response_message = f"Order received for {quantity} units of {symbol} on {exchange} exchange to SELL."

    response = {
        "message": response_message
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)

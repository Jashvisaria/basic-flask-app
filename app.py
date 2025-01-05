from flask import Flask, render_template

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html', title="Open Terminal", slogan="Empowering Traders with Insight and Simplicity")

# Route for the about page
@app.route('/about')
def about():
    return render_template('about.html', title="About Open Terminal", slogan="Learn more about our features")

if __name__ == '__main__':
    app.run(debug=True)

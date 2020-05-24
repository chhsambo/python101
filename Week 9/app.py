from flask import Flask


app = Flask(__name__)   # Flask application 

# decorators
@app.route('/home')
def home():
    return 'Welcome to very first Flask website'


@app.route('/about')
def about():
    return '<h1>About Us</h1>'


app.run()

# To test flask http://localhost:5000
from flask import Flask, render_template


app = Flask(__name__)   # Flask application


@app.route('/')
def home_page():
    contact_list = [
        {
            'name': 'Sok',
            'phone': '012',
            'facebook': 'fb.com/sok'
        },
        {
            'name': 'Sau',
            'phone': '013',
            'facebook': 'fb.com/sau'
        },
        {
            'name': 'Minea',
            'phone': '016',
            'facebook': 'fb.com/minea'
        }
    ]
    return render_template('index.html', contacts=contact_list)


@app.route('/add')
def add_contact():
    return render_template('add.html')


app.run(debug=True)

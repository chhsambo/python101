import os

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)   # Flask application
app.config['SQLALCHEMY_DATABASE_URI'] = (
    'sqlite:///' + os.path.join(basedir, 'data', 'database1.db')
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)    # Database


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    phone = db.Column(db.String(120), nullable=True)
    facebook = db.Column(db.String(120), nullable=True)

    def __repr__(self):
        return '<Contact: %r>' % self.name


@app.route('/')
def home_page():
    contact_list = Contact.query.all()
    
    return render_template('index.html', contacts=contact_list)


@app.route('/add')
def add_contact():
    return render_template('add.html')


if __name__ == '__main__':
    app.run(debug=True)

from flask import render_template

from application import app
from application.models import Contact, Note


@app.route('/')
def home_page():
    contact_list = Contact.query.all()

    notes = Note.query.all()

    return render_template('index.html', contacts=contact_list)


@app.route('/add')
def add_contact():

    return render_template('add.html')

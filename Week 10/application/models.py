from . import db


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    phone = db.Column(db.String(120), nullable=True)
    facebook = db.Column(db.String(120), nullable=True)

    def __repr__(self):
        return '<Contact: %r>' % self.name


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    contact_id = db.Column(db.Integer, db.ForeignKey('contact.id'), nullable=False)
    note = db.Column(db.String(1000), nullable=False)

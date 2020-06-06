from main import db


def init_db():
    db.create_all()

    sok = Contact(id=1, name='Sok', phone='012', facebook='fb.com/sok')
    sau = Contact(id=2, name='Sau', phone='013', facebook='fb.com/sau')
    minea = Contact(id=3, name='Minea', phone='016', facebook='fb.com/minea')

    db.session.add(sok)
    db.session.add(sau)
    db.session.add(minea)
    db.session.commit()


init_db()

print("New Database Created!!!")
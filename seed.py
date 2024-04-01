"""Seed file for adoption_agency db"""

# (venv) python seed.py --> runs this file

from models import Pet, db
from app import app

# create all tables
with app.app_context():
    db.drop_all()
    db.create_all()

    Pet.query.delete()

# add users
scooby = Pet(name='Scooby', species='dog', age=9, photo_url='https://thumbor.bigedition.com/great-dane/ws7Ah1sICHFmsi2v4N29_J5Fpgw=/800x0/filters:quality(80)/granite-web-prod/3e/7c/3e7c7de4470149dbb6dfe7cccc76ef8a.jpeg')
rocket = Pet(name='Rocket', species='cat', age=5, notes='very hyper, will bounce off the walls if given catnip', photo_url='https://media.istockphoto.com/id/1361394182/photo/funny-british-shorthair-cat-portrait-looking-shocked-or-surprised.jpg?b=1&s=612x612&w=0&k=20&c=-niqIUX8Kfiyn50xgUzxxUYX6H2q9BlGc3PX5PVM-iA=')
fred = Pet(name='Fred', species='porcupine', photo_url='https://brevardzoo.org/wp-content/uploads/2020/11/Shelley-2.jpg')
cupcake = Pet(name='Cupcake', species='cat', available=False)

with app.app_context():
    db.session.add(scooby)
    db.session.add(rocket)
    db.session.add(fred)
    db.session.add(cupcake)

    db.session.commit()
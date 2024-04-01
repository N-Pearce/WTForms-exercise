from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, NumberRange

class AddPetForm(FlaskForm):
    """Form to add a pet"""

    name = StringField("Pet Name",
                       validators=[InputRequired()])
    species = SelectField("Species",
                       choices=[('cat', "Cat"), ('dog', "Dog"), ('porcupine', "Porcupine")])
    photo_url = StringField("Photo URL",
                       validators=[Optional(), URL()])
    age = IntegerField("Age",
                       validators=[Optional(), NumberRange(0,30)])
    notes = TextAreaField("Notes",
                       validators=[Optional()])
    
class EditPetForm(FlaskForm):
    """Form to edit a pet"""

    photo_url = StringField("Photo URL",
                       validators=[Optional(), URL()])
    notes = TextAreaField("Notes",
                       validators=[Optional()])
    available = BooleanField("Available",
                             validators=[Optional()])
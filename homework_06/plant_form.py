from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired, Length


class PlantForm(FlaskForm):
    name = StringField("Plant name", name="plant_name", validators=[
        DataRequired(),
        Length(min=2),
    ])
    type = SelectField("Plant type", name="plant_type", choices=[
        ("seaweed", u"Водоросли"),
        ("moss", u"Мхи"),
        ("fern", u"Папоротники"),
        ("blooming", u"Цветковые"),
        ("coniferous", u"Хвойные")],
        validators=[DataRequired()]
    )
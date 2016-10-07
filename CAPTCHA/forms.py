
from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class CaptchaForm(Form):
    captcha = StringField('Captcha', validators=[DataRequired()])

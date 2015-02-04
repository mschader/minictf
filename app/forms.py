from flask.ext.wtf import Form
from wtforms import PasswordField, SubmitField
from wtforms.validators import DataRequired


class GettingStartedForm(Form):
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')

    def validate(self):
        if self.password.data == "abc":
            return True
        else:
            return False
from wtforms import Form, StringField,  PasswordField
from wtforms.validators import Length,  DataRequired,  ValidationError

from app.models.user import User

class RegisterForm(Form):
    name = StringField(validators=[DataRequired(), Length(2, 8)])

    password = PasswordField(validators=[
        DataRequired(), Length(2, 8)
    ])

    def validate_name(self, field):
        if User.query.filter_by(name=field.data).first():
            raise ValidationError('用户名已存在')

class LoginForm(Form):
    name = StringField(validators=[DataRequired(), Length(2, 8)])
    password = PasswordField(validators=[
        DataRequired(), Length(2, 8)
    ])


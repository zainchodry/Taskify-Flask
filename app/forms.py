from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField
from wtforms.validators import DataRequired, Length


class RegisterForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired(), Length(min=4, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')



class LoginForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired()])
    submit = SubmitField('Login')



class TaskForm(FlaskForm):
    title = StringField('Task Title', validators = [DataRequired()])
    due_date = DateField('Due Date' , format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField('Add Task')




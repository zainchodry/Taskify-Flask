from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app.models import User, Task
from app.forms import RegisterForm, LoginForm, TaskForm
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')



@main.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        user = User(username=form.username.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Registered successfully!', 'success')
        return redirect(url_for('main.login'))
    
    return render_template('register.html', form = form)



@main.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('Logged in successfully!', 'success')
            return redirect(url_for('main.dashboard'))
        
        flash('Login Unsuccessful. Please check username and password', 'danger')

    return render_template('login.html', form = form)



@main.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('main.index'))


@main.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(title=form.title.data, due_date=form.due_date.data, owner=current_user)
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('main.dashboard'))

    search = request.args.get('search')
    tasks = Task.query.filter(Task.owner == current_user)
    if search:
        tasks = tasks.filter(Task.title.contains(search))

    return render_template('dashboard.html', form=form, tasks=tasks.all())




@main.route('/delete/<int:id>')
@login_required
def delete(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('main.dashboard'))


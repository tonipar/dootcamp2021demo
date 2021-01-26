from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')

@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    rounds = [
        {
            'course': {'coursename': 'Puijo DGP'},
            'score': '-1'
        },
        {
            'course': {'coursename': 'Peltosalmi DGP'},
            'score': '-4'
        }
    ]
    return render_template('index.html', title='Home', user=user, rounds=rounds)

@app.route('/login')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remeber_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
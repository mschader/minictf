from flask import render_template, request, url_for, redirect, flash
from .forms import GettingStartedForm
from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/gettingStarted', methods=['GET', 'POST'])
def getting_started():
    form = GettingStartedForm()
    if request.method == 'POST':
        if not form.validate():
            flash('Wrong Password')
            return render_template('gettingStarted.html', form=form)
        else:
            return redirect(url_for('success'))
    return render_template('gettingStarted.html',
                           form=form)


@app.route('/success')
def success():
    return render_template('success.html')
from flask import Flask, render_template, request, url_for, redirect, flash
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField
from wtforms.validators import DataRequired, Email
import smtplib
import os

class EmailForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    message = StringField('Message', validators=[DataRequired()])


app = Flask(__name__)
app.secret_key = 'SDSADDAS231DSA123EFWQ'


@app.route('/', methods=['POST', 'GET'])
def home():
    form = EmailForm()
    if form.validate_on_submit():
        flash("Your message was sent!")
        return redirect(url_for('home'))
    return render_template('index.html', form=form)



if __name__ == "__main__":
    app.run()
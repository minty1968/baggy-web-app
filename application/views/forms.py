"""Routes for base pages."""
from flask import Blueprint, redirect, render_template, flash, request, session, url_for
from flask_login import login_required, logout_user, current_user, login_user
from wtforms.validators import email
from application.models.forms import LoginForm, RegistrationForm, ContactForm

# Blueprint Configuration
formsBP = Blueprint('forms', __name__,
                      template_folder='application/templates',
                      static_folder='application/static', url_prefix='/forms')


@formsBP.route('/login', methods=['GET', 'POST'])
def login():
    """
    Log-in page for registered users.

    GET requests serve Log-in page.
    POST requests validate and redirect user to dashboard.
    """
    form = LoginForm()

    return render_template('forms/login.html', form=form, template="form-template", 
                           body="Login Form", title='Sharpe Digital Solutions')


@formsBP.route("/register", methods=["GET", "POST"])
def register():
    """
    User Registration page.

    GET requests serve sign-up page.
    POST requests validate form & user creation.
    """
    
    form = RegistrationForm()

    return render_template("forms/register.html", form=form, template="form-template", 
                           body="Registration Form", title='Sharpe Digital Solutions')


@formsBP.route("/contact", methods=["GET", "POST"])
def contact():
    """Standard `contact` form."""

    form = ContactForm()
    
    return render_template("forms/contact.html", form=form, template="form-template", 
                           body="Contact Form", title='Sharpe Digital Solutions')

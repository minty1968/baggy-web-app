"""Routes for password generator pages."""
from flask import Blueprint, render_template, request
from application.models.password import Password

# Blueprint Configuration
passwdBP = Blueprint('password', __name__,
                        template_folder='application/templates/password/',
                        static_folder='static')


@passwdBP.route('/password', methods=['GET', 'POST'])
def passwd():
    """Password route."""
    
    return render_template('password/passwd.html', body="Password Generator",
                           title='Sharpe Digital Solutions | Password Generator')
                        
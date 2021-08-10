"""Initialize app."""
from flask import Flask


def create_app():
    """Construct the core application."""
    app = Flask(__name__)
    # Application Configuration
    app.config.from_object('config.Config')

    with app.app_context():
        # Import parts of our application
        from application.views.base import baseBP
        from application.views.lottery import lotteryBP
        from application.views.password import passwdBP
        from application.views.games import gamesBP
        from application.views.forms import formsBP
        
        # Register Blueprints
        app.register_blueprint(baseBP)
        app.register_blueprint(lotteryBP)
        app.register_blueprint(passwdBP)
        app.register_blueprint(gamesBP)
        app.register_blueprint(formsBP)
        return app

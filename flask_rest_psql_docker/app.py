from flask import Flask

from .extensions import db, ma
from flask_rest_psql_docker.api.models import People
from flask_rest_psql_docker.api.routes import api_bp


def create_app(config='flask_rest_psql_docker.settings'):
    app = Flask(__name__)
    app.config.from_object(config)

    load_extension(app)
    register_blueprints(app)
    register_shellcontext(app)

    return app


def load_extension(app):
    """ Register Extensions. """
    db.init_app(app)
    ma.init_app(app)
    return None


def register_blueprints(app):
    """ Register Blueprints. """
    app.register_blueprint(
        api_bp,
        url_prefix='{}'.format(app.config['URL_PREFIX'])
    )
    return None


def register_shellcontext(app):
    """Register shell context objects. Use Shell to create dummy user"""
    def shell_context():
        """Shell context objects."""
        return {
            'db': db,
            'People': People,
        }

    app.shell_context_processor(shell_context)
    return None

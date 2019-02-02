from flask import Blueprint
from flask_restplus import Api

# don't use the same name for blueprint instances.
web_bp = Blueprint('website', __name__)
api = Api(web_bp)


@web_bp.route('/')
def homepage():
    return('hello')


@web_bp.route('/dogs/')
def dog():
    return('dogs')

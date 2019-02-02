from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/db'
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Register blueprints; import below db to avoid circular errors
from flask_rest_psql_docker.api.routes import blueprint as api
from flask_rest_psql_docker.website.routes import blueprint as website

app.register_blueprint(api, url_prefix='/api')
app.register_blueprint(website, url_prefix='')




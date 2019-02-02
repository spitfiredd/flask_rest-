from flask import Blueprint, jsonify
from flask_restplus import Api, Resource


api_bp = Blueprint('api', __name__)
api = Api(api_bp)

ns_ppl = api.namespace('people', description='People Information')
ns_dogs = api.namespace('dogs', description='Dog Information')


@ns_ppl.route("/")
class PeopleList(Resource):
    def get(self):
        """
        returns a list of people
        """
        from .models import People, PeopleSchema

        person = People.query.first()
        schema = PeopleSchema()
        output = schema.dump(person).data

        return jsonify({'user': output})

    def post(self):
        """
        Adds a new person to the list
        """


@ns_ppl.route("/<int:id>")
class People(Resource):
    def get(self, id):
        """
        Displays a person's details
        """
        from .models import People, PeopleSchema

        # removed f-string, id is an int, no need to cast
        person = People.query.filter_by(id=id).first()
        schema = PeopleSchema()
        output = schema.dump(person).data

        return jsonify({'user': output})

    def put(self, id):
        """
        Edits a selected person
        """


@ns_dogs.route("/")
class DogsList(Resource):
    def get(self):
        """
        returns a list of dogs
        """
    def post(self):
        """
        Adds a new dog to the list
        """


@ns_dogs.route("/<int:id>")
class Dogs(Resource):
    def get(self, id):
        """
        Displays a dog's details
        """
    def put(self, id):
        """
        Edits a selected dog
        """

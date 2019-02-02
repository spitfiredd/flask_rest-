from flask_rest_psql_docker.extensions import db, ma


class People(db.Model):  # Table name is set to lowercase of the class name
    """Run from project level dir

    `python3`
    `from flask_rest_psql_docker import db`
    `db.create_all()`

    if you want to insert data manually:

    `from flask_rest_psql_docker.models import People`
    `p = People(first='', last='', school='', job='', age='')`
    """
    id = db.Column(db.Integer, primary_key=True)
    first = db.Column(db.String(80))
    last = db.Column(db.String(80))
    school = db.Column(db.String(80))
    job = db.Column(db.String(80))
    age = db.Column(db.Integer, nullable=False)

    # Removed init method, its no really necessary

    def __repr__(self):
        return "<User(first='%s', last='%s', school='%s', job='%s', age='%d')>" % (
            self.first, self.last, self.school, self.job, self.age)


class PeopleSchema(ma.ModelSchema):
    class Meta:
        model = People

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Student(Resource):

    def get(self, name):
        return {'student': name} # we do not need to jsonify the dictionaries as flash_restful does that for us

# add_resource is used to define resources of a API and the path, instead of using the static method "@app.route"
api.add_resource(Student, '/student/<string:name>') #http://127.0.0.1:5000/student/Rolf


app.run(port=5000)

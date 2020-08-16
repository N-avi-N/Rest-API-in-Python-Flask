from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help='enter username')
    parser.add_argument('password', type=str, required=True, help='enter password')

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": 'Username already present'}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {'message': 'user created successfully.'}, 201
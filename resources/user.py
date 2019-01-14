from flask_restful import Resource, reqparse
from models.user import UserModel 

class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be blank!")
    parser.add_argument('password',
        type=str,
        required=True,
        help="This field cannot be blank!")

    def post(self):
        data = UserRegister.parser.parse_args()
        if UserModel.find_by_username(data['username']) is None:
            user = UserModel(**data)
            return {"message": "User created successfully"}, 201
        
        return {"message": "User already exists"}, 400

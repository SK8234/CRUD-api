from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

# Example in-memory database (dictionary)
db = {
    1: {"name": "ajay", "age": 12},
    2: {"name": "jay", "age": 23}}

# POST request argument parser
post_args = reqparse.RequestParser()
post_args.add_argument("name", type=str, help="name is required", required=True)
post_args.add_argument("age", type=int, help="age is required", required=True)

class Todo(Resource):
    def post(self, db_id):
        if db_id in db:
            return {"message": f"Task ID {db_id} is already present, name: {db[db_id]['name']}"}, 400
        args = post_args.parse_args()  # Parse incoming data
        db[db_id] = {"name": args["name"], "age": args["age"]}
        return db[db_id], 201  # Return created task and HTTP status 201 (Created)
    
api.add_resource(Todo, '/db/<int:db_id>')  # Handle individual tasks

if __name__ == '__main__':
    app.run(debug=True)

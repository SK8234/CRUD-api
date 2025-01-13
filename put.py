from flask import Flask
from flask_restful import Resource, Api, reqparse, abort

app = Flask(__name__)
api = Api(app)

# In-memory database (dictionary)
db = {
    1: {"name": "ajay", "age": 12},
    2: {"name": "jay", "age": 23}
}

put_args = reqparse.RequestParser()
put_args.add_argument("name", type=str)
put_args.add_argument("age", type=int)


class Todo(Resource):
    def put(self, db_id):
        if db_id not in db:
            return {"message": f"Task ID {db_id} not found"}, 404

        args = put_args.parse_args()  # Parse incoming data for update
        if args['name']:
            db[db_id]['name'] = args["name"]
        if args['age']:
            db[db_id]['age'] = args["age"]
        return db[db_id], 200  # Return updated task and HTTP status 200 (OK)


# Define resources for the routes
api.add_resource(Todo, '/db/<int:db_id>')  # Handle individual tasks

if __name__ == '__main__':
    app.run(debug=True)

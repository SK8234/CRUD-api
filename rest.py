from flask import Flask
from flask_restful import Resource, Api, reqparse, abort

app = Flask(__name__)
api = Api(app)

# In-memory database (dictionary)
db = {
    1: {"name": "ajay", "age": 12},
    2: {"name": "jay", "age": 23}
}

# POST request argument parser
post_args = reqparse.RequestParser()
post_args.add_argument("name", type=str, help="name is required", required=True)
post_args.add_argument("age", type=int, help="age is required", required=True)

# PUT request argument parser
put_args = reqparse.RequestParser()
put_args.add_argument("name", type=str)
put_args.add_argument("age", type=int)

# Resource to get all tasks
class Todo_list(Resource):
    def get(self):
        return db

# Resource to handle individual tasks (GET, POST, PUT, DELETE)
class Todo(Resource):

    # GET: Fetch a task by its ID
    def get(self, db_id):
        task = db.get(db_id)
        if task is None:
            return {"message": "Not found"}, 404
        return task, 200

    # POST: Create a new task (if ID doesn't already exist)
    def post(self, db_id):
        if db_id in db:
            return {"message": f"Task ID {db_id} is already present, name: {db[db_id]['name']}"}, 400
        args = post_args.parse_args()  # Parse incoming data
        db[db_id] = {"name": args["name"], "age": args["age"]}
        return db[db_id], 201  # Return created task and HTTP status 201 (Created)

    # DELETE: Remove a task by its ID
    def delete(self, db_id):
        if db_id not in db:
            return {"message": f"Task ID {db_id} not found"}, 404
        del db[db_id]  # Delete task from the database
        return {"message": "Task deleted successfully"}, 200

    # PUT: Update an existing task (if ID exists)
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
api.add_resource(Todo_list, '/db')  # Handle list of tasks

if __name__ == '__main__':
    app.run(debug=True)

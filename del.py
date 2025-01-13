from flask import Flask
from flask_restful import Resource, Api, reqparse, abort

app = Flask(__name__)
api = Api(app)

# In-memory database (dictionary)
db = {
    1: {"name": "ajay", "age": 12},
    2: {"name": "jay", "age": 23}
}

class Todo(Resource):
    def delete(self, db_id):
        if db_id not in db:
            return {"message": f"Task ID {db_id} not found"}, 404
        del db[db_id]  # Delete task from the database
        return {"message": "Task deleted successfully"}, 200
    
api.add_resource(Todo, '/db/<int:db_id>')  # Handle individual tasks


if __name__ == '__main__':
    app.run(debug=True)


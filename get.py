from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

# Example in-memory database (dictionary)
db = {
    1: {"name": "ajay", "age": 12},
    2: {"name": "jay", "age": 23}
}

class Todo_list(Resource):
    def get(self):
        return db

class Todo(Resource):
    # GET: Fetch a task by its ID
    def get(self, db_id):
        task = db.get(db_id)
        if task is None:
            return {"message": "Not found"}, 404
        return task, 200
    
api.add_resource(Todo, '/db/<int:db_id>')
api.add_resource(Todo_list, '/db')

if __name__ == '__main__':
    app.run(debug=True)


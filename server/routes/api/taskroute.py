from flask import request, jsonify, Flask, Blueprint
from models.task import Task
from config.connection import Session

app = Flask(__name__)

task_api = Blueprint('task_api', __name__)

@app.route('/api/tasks', methods=['POST'])
def create_task():
    # Get task data from the request body
    data = request.json

    # Create a new task
    new_task = Task(title=data['title'], description=data.get('description', ''))

    # Add the task to the session and commit it to the database
    Session.add(new_task)
    Session.commit()

    # Return the created task as JSON response
    return jsonify({"message": "Task created successfully", "task": new_task.to_dict()}), 201

if __name__ == '__main__':
    app.run(debug=True)






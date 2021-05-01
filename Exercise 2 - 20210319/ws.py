# flask/bin/python
import os
from flask import abort
from flask import Flask, jsonify, request, render_template

# Flask import for database
from flask_sqlalchemy import SQLAlchemy

# Create Flask-app and Database
app = Flask(__name__)

# Setup configuration
from config import Config
app.config.from_object(Config)

# Setup database link
db = SQLAlchemy(app)

# A list of tasks
tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    },
    {
        'id': 3,
        'title': u'Reading',
        'description': u'Read a book',
        'done': False
    }
]


# Routes
@app.route('/')
def home():
    return render_template('index.html')

# GET Functions
@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]

    if len(task) == 0:
        abort(404)

    return jsonify({'task': task[0]})

# POST Functions
@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': task[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

# PUT Functions
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]

    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    # if 'title' in request.json:# and type(request.json['title']) != unicode:
    #     abort(400)
    # if 'description' in request.json:# and type(request.json['description']) is not unicode:
    #     abort(400)
    # if 'done' in request.json:# and type(request.json['done']) is not bool:
    #     abort(400)
    
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])

    return jsonify({'task': task[0]})

# DELETE Functions
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]

    if len(task) == 0:
        abort(404)

    tasks.remove(task[0])
    return jsonify({'result': True})

# Error Handling
from flask import make_response

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}, 404))


# Driver
if __name__ == "__main__":
    app.run(debug=True)

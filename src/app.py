from flask import Flask, jsonify, request
import json

app = Flask(__name__)

todos = [
            { "label": "My first task", "done": False},
            { "label": "My second task", "done": False}
        ]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)        
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    decoded_object = json.loads(request.data)
    todos.append(decoded_object)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    del todos[position]
    return jsonify(todos)

#Server definition
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
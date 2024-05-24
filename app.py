from flask import Flask, render_template, request, redirect, url_for, jsonify
from datetime import datetime

app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    task_name = request.form.get('taskName')
    task_desc = request.form.get('taskDesc')
    deadline = request.form.get('deadline')
    
    if task_name:
        tasks.append({'task': task_name, 'desc': task_desc, 'deadline': deadline})
    
    return redirect(url_for('index'))

@app.route('/remove_task', methods=['POST'])
def remove_task():
    task_index = int(request.form.get('taskIndex'))
    if 0 <= task_index < len(tasks):
        tasks.pop(task_index)
    
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)

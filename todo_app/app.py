from flask import Flask, redirect, request
from flask import render_template
import os

from todo_app.flask_config import Config
from todo_app.data.trello_items import get_items, add_item, change_item_list
from todo_app.models.view_model import ViewModel

app = Flask(__name__)
app.config.from_object(Config())

@app.route('/')
def index():
    item_view_model = ViewModel(get_items())
    return render_template('index.html', view_model=item_view_model)

@app.route('/add', methods=['POST'])
def add():
    add_item(request.form.get('task_title'))
    return redirect("/")

@app.route('/completed/<id>')
def completed_item(id):
  change_item_list(id, os.getenv('TRELLO_COMPLETED_LIST'))
  return redirect("/")

@app.route('/in-progress/<id>')
def in_progress_item(id):
  change_item_list(id, os.getenv('TRELLO_IN_PROGRESS_LIST'))
  return redirect("/")

@app.route('/not-started/<id>')
def not_started_item(id):
  change_item_list(id, os.getenv('TRELLO_NOT_STARTED_LIST'))
  return redirect("/")
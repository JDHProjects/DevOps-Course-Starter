"""Main file for todo app."""

import os
from flask import Flask, redirect, request
from flask import render_template

from todo_app.flask_config import Config
from todo_app.data.trello_items import Items
from todo_app.models.view_model import ViewModel

def create_app():
  """Run Flask app."""
  app = Flask(__name__)
  app.config.from_object(Config())

  board_items = Items()

  @app.route('/')
  def index():
    item_view_model = ViewModel(board_items.items)
    return render_template('index.html', view_model=item_view_model)

  @app.route('/add', methods=['POST'])
  def add():
    board_items.add_item(request.form.get('task_title'))
    return redirect("/")

  @app.route('/completed/<card_id>')
  def completed_item(card_id):
    board_items.change_item_list(card_id, os.getenv('TRELLO_COMPLETED_LIST'))
    return redirect("/")

  @app.route('/in-progress/<card_id>')
  def in_progress_item(card_id):
    board_items.change_item_list(card_id, os.getenv('TRELLO_IN_PROGRESS_LIST'))
    return redirect("/")

  @app.route('/not-started/<card_id>')
  def not_started_item(card_id):
    board_items.change_item_list(card_id, os.getenv('TRELLO_NOT_STARTED_LIST'))
    return redirect("/")

  return app

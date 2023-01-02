from flask import Flask, redirect, request
from flask import render_template

from todo_app.flask_config import Config
from todo_app.data.session_items import get_items, add_item
import sys

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    return render_template('index.html', tasks=get_items())

@app.route('/add', methods=['POST'])
def add():
    add_item(request.form.get('task_title'))
    return redirect("/")
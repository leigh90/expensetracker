from peach.main import leblueprint
from flask import render_template

@leblueprint.route('/')
def index():
    return render_template('index.html')
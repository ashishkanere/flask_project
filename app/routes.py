from flask import render_template
from . import create_app

app = create_app()

@app.route('/')
def home():
    return "Hello, Flask!"

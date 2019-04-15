from flask import Flask, render_template
from f2eMid import app

@app.route('/')
def index():
    return render_template('index.html')

from flask import Flask, jsonify, render_template, request
import sys
sys.path.append(sys.path[0] + '/src/')
from src.remote import Remote

remote = Remote()
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/youtube')
def youtube():
    remote.youtube()
    return jsonify(result='success')

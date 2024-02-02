from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route("/")
def home_page():
  return render_template('index.html')

@app.route("/calculate", methods=['POST'])
def calculate():
  data = request.get_json()
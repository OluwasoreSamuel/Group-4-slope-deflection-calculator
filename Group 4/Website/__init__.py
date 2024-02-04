from flask import Flask, render_template, Blueprint, jsonify, make_response, request



def create_app():
  app = Flask(__name__)
  app.config["SECRET_KEY"] = "groupfour"
  
  return app
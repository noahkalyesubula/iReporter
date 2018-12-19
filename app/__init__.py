from flask import Flask

# create an instance of Flask
app = Flask(__name__)

from app.routes.redflag_urls import Routes
Routes.fetch_urls(app)
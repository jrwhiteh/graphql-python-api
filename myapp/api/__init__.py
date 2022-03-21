from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask import request
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("PSQL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)



@app.route('/')
def test():
    return 'home'
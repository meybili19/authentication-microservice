from flask import Flask, render_template
from flask_cors import CORS
from src.config.config import Config
from src.models.models import db
from src.routes.routes import authenticate_user


app = Flask(__name__,  static_folder='FRONTEND')

CORS(app)


app.config.from_object(Config)


db.init_app(app)


@app.route('/')
def home():
    return "Home Page - Please login first"


@app.route('/login', methods=['POST'])
def login_route():
    return authenticate_user()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004, debug=True)

from flask import Flask, abort, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, Article
from datetime import datetime
import os
import dotenv

dotenv.load_dotenv()

ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD")

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_KEY')
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_URI")
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"
db.init_app(app)
Bootstrap5(app)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/good')
def good():
    return render_template('good.html')
@app.route('/paiment')
def paiment():
    return render_template('paiment.html')





if __name__ == "__main__":
    app.run(debug=True, port=5000)

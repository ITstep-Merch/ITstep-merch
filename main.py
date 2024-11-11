from flask import Flask, abort, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, Good
from datetime import datetime
import os
import dotenv

dotenv.load_dotenv()

ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD")

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_KEY')
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_URI")
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///merch.db"
db.init_app(app)
Bootstrap5(app)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    all_goods = db.session.execute(db.select(Good).order_by(Good.id.desc())).scalars().all()
    return render_template('home.html', all_goods=all_goods)

@app.route('/good')
def good():
    return render_template('good.html')

@app.route('/payment')
def payment():
    return render_template('payment.html')

@app.route('/admin/<password>', methods=["GET", "POST"])
def admin(password):
    if password == ADMIN_PASSWORD:
        if request.method == "POST":
            new_good = Good(
                name=request.form.get('name'),
                img_url=request.form.get('img_url'),
                code=request.form.get('code'),
                price=request.form.get('price'),
                color=request.form.get('color'),
                size=request.form.get('size'),
                description=request.form.get('description'),
                made_of=request.form.get('made_of'),
            )
            db.session.add(new_good)
            db.session.commit()

            render_template('admin.html', password=password)
            
        return render_template('admin.html', password=password)
    else: 
        return abort(403)
    
@app.route('/admin/home/<password>', methods=["GET", "POST"])
def admin_home(password):
    if password == ADMIN_PASSWORD:
        if request.method == "POST":
            new_good = Good(
                name=request.form.get('name'),
                img_url=request.form.get('img_url'),
                code=request.form.get('code'),
                price=request.form.get('price'),
                color=request.form.get('color'),
                size=request.form.get('size'),
                description=request.form.get('description'),
                made_of=request.form.get('made_of'),
            )
            db.session.add(new_good)
            db.session.commit()

            render_template('admin.html', password=password)
            
        return render_template('admin.html', password=password)
    else: 
        return abort(403)





if __name__ == "__main__":
    app.run(debug=True, port=5000)

from flask import Flask, abort, render_template, redirect, url_for, flash, jsonify, request
from flask_bootstrap import Bootstrap5
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, Good
from datetime import datetime
import os
import dotenv
import requests

dotenv.load_dotenv()

ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD")

API_KEY = os.environ.get('NOVA_POSHTA_API_KEY')
print(API_KEY)

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

@app.route('/good/<id>')
def good(id):
    good = db.session.execute(db.select(Good).where(Good.id == id)).scalar_one()
    return render_template('good.html', good=good)

@app.route('/get_good/<int:id>')
def get_good(id):
    get_good = db.session.execute(db.select(Good).where(Good.id == id)).scalar_one()
    return jsonify({
        "id": get_good.id,
        "name": get_good.name,
        "price": get_good.price,
        "src": get_good.img_url_front,
        "code":get_good.code,
        "color": get_good.color,
        "size": get_good.size
    })

@app.route('/get_good_cart/cart-<int:id>')
def get_good_cart(id):
    get_good = db.session.execute(db.select(Good).where(Good.id == id)).scalar_one()
    return jsonify({
        "id": get_good.id,
        "name": get_good.name,
        "price": get_good.price,
        "src": get_good.img_url_front,
        "code":get_good.code,
        "color": get_good.color,
        "size": get_good.size
    })

@app.route('/payment')
def payment():
    return render_template('payment.html')

@app.route('/admin/<password>', methods=["GET", "POST"])
def admin(password):
    if password == ADMIN_PASSWORD:
        if request.method == "POST":
            new_good = Good(
                name=request.form.get('name'),
                img_url_front=request.form.get('img_url_front'),
                img_url_back=request.form.get('img_url_back'),
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
     
@app.route('/get_warehouses', methods = ["GET", "POST"])
def get_warehouses():
    dataFromPOST = request.get_json() 
    url = "https://api.novaposhta.ua/v2.0/json/"
    payload = {
        "apiKey": API_KEY,
        "modelName": "AddressGeneral",
        "calledMethod": "getWarehouses",
        "methodProperties": {
            "CityName" : "Київ",
            "Page" : "1",
            "Limit" : "50",
            "Language" : "UA",
        }
    }

    try:
        res = requests.post(url, json=payload)
        res.raise_for_status()
        res_data = res.json()
        return jsonify(res_data.get("data", []))
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500







if __name__ == "__main__":
    app.run(debug=True, port=5000)

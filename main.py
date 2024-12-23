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
     
@app.route('/get_warehouses', methods = ["POST"])
def get_warehouses():
    dataFromPOST = request.get_json() 
    city_name = dataFromPOST.get("CityName", "Київ")  # Значення за замовчуванням
    page = dataFromPOST.get("Page", "1")
    limit = dataFromPOST.get("Limit", "50")
    language = dataFromPOST.get("Language", "UA")

    print(dataFromPOST)
    url = "https://api.novaposhta.ua/v2.0/json/"
    payload = {
        "apiKey": API_KEY,
        "modelName": "AddressGeneral",
        "calledMethod": "getWarehouses",
        "methodProperties": {
            "CityName" : city_name,
            "Page" : page,
            "Limit" : limit,
            "Language" : language,
        }
    }

    try:
        res = requests.post(url, json=payload)
        res.raise_for_status()
        res_data = res.json()
        return jsonify(res_data.get("data", []))
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/get_oblast', methods=["GET"])
def get_oblast():
    url = "https://api.novaposhta.ua/v2.0/json/"
    payload = {
        "apiKey": API_KEY,
        "modelName": "AddressGeneral",
        "calledMethod": "getSettlementAreas",
        "methodProperties": {
            "Ref" : ""
        }
    }
    # {
    #     "apiKey": API_KEY,
    #     "modelName": "AddressGeneral",
    #     "calledMethod": "getAreas",
    #     "methodProperties": {   }
    # }
    


    try:
        res = requests.post(url, json=payload)
        res.raise_for_status()
        res_data = res.json()
        return jsonify(res_data.get("data", []))
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500
    

    
@app.route('/get_city_in_oblast', methods=["GET"])
def get_city_in_oblast():
    RefOblast = request.args.get('RefOblast')
    InputByUser_City = request.args.get('InputByUser_City')
    url = "https://api.novaposhta.ua/v2.0/json/"
    payload =     {
        "apiKey": API_KEY,
        "modelName": "AddressGeneral",
        "calledMethod": "getSettlements",
        "methodProperties": {
            "AreaRef": RefOblast,
            "FindByString" : InputByUser_City,
            "Limit": "100"
        }
    }
    # {
    #     "apiKey": API_KEY,
    #     "modelName": "Address",
    #     "calledMethod": "getCities",
    #     "methodProperties": 
    #     {
    #         "FindByString": InputByUser_City,
    #         "AreaRef" : RefOblast  # Додаємо Ref області як фільтр
    #     }
    # }
    # payload = {
    #     "apiKey": API_KEY,
    #     "modelName": "Address",
    #     "calledMethod": "getCities",
    #     "methodProperties": 
    #     {
    #         "FindByString": InputByUser_City,
    #         "RegionRef": RefOblast  # Додаємо Ref області як фільтр
    #     }
    # }
    


    try:
        res = requests.post(url, json=payload)
        res.raise_for_status()
        res_data = res.json()

        return jsonify(res_data.get("data", []))
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500
    

@app.route('/get_street_in_city', methods=["GET"])
def get_street_in_city():
    RefCity = request.args.get('RefCity')
    InputByUser_Street = request.args.get('InputByUser_Street')

    url = "https://api.novaposhta.ua/v2.0/json/"
    payload = {
        "apiKey": API_KEY,
        "modelName": "AddressGeneral",
        "calledMethod": "getStreet",
        "methodProperties": {
            "CityRef" : RefCity,
            "FindByString" : InputByUser_Street,
            "Limit" : "300"
        }
    }


    try:
        res = requests.post(url, json=payload)
        res.raise_for_status()
        res_data = res.json()
        print(res_data)
        return jsonify(res_data.get("data", []))
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/get_wareHouse_in_city_streetAd', methods=["GET"])
def get_wareHouse_in_city_streetAd():
    nameCity = request.args.get('nameCity')
    InputByUser_House = request.args.get('InputByUser_House')
    print("nameCity",nameCity)
    print("InputByUser_House",InputByUser_House)

    url = "https://api.novaposhta.ua/v2.0/json/"
    # payload = {
    #     "apiKey": API_KEY,
    #     "modelName": "AddressGeneral",
    #     "calledMethod": "getWarehouses",
    #     "methodProperties": {
    #         "FindByString" : InputByUser_House,
    #         "CityName" : nameCity,
    #         "CityRef" : " ",
    #         "Page" : "",
    #         "Limit" : "50",
    #         "Language" : "UA",
    #         "TypeOfWarehouseRef" : "",
    #         "WarehouseId" : ""
    #     }
    # }

    payload = {
        "apiKey": API_KEY,
        "modelName": "AddressGeneral",
        "calledMethod": "getWarehouses",
        "methodProperties": {
                "FindByString" : InputByUser_House,
                "CityName" : nameCity,
                "CityRef" : "",
                "Page" : "",
                "Limit" : "20",
                "Language" : "UA",
                "TypeOfWarehouseRef" : "",
                "WarehouseId" : ""
            }
    }


    try:
        res = requests.post(url, json=payload)
        res.raise_for_status()
        res_data = res.json()
        print(res_data)
        return jsonify(res_data.get("data", []))
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500




if __name__ == "__main__":
    app.run(debug=True, port=5000)

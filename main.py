from flask import Flask, abort, render_template, redirect, url_for, jsonify, request, send_from_directory
from flask_bootstrap import Bootstrap5
from models import db, Good
import os
import dotenv
import requests
from email_manager import Email

dotenv.load_dotenv()

ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD")
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")
POST_EMAIL = os.environ.get("POST_EMAIL")
POST_PASSWORD = os.environ.get("POST_PASSWORD")

API_KEY = os.environ.get('NOVA_POSHTA_API_KEY')
print(API_KEY)

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_KEY')
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
        "color": get_good.color 
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
    })

@app.route('/payment')
def payment():
    return render_template('payment.html')

@app.route('/policy')
def policy():
    return render_template('policy.html')

@app.route('/admin/<password>', methods=["GET", "POST"])
def admin(password):
    if password == ADMIN_PASSWORD:
        if request.method == "POST":

            def convert_drive_url_to_thumbnail(url):
                if "/file/d/" in url and "/view" in url:
                    file_id = url.split("/file/d/")[1].split("/view")[0]
                    thumbnail_url = f"https://drive.google.com/thumbnail?id={file_id}&sz=w400"
                    return thumbnail_url
                else:
                    print("Невірний формат посилання")
                    return

            new_good = Good(
                name=request.form.get('name'),
                img_url_front=convert_drive_url_to_thumbnail(request.form.get('img_url_front')),
                img_url_back=convert_drive_url_to_thumbnail(request.form.get('img_url_back')),
                code=request.form.get('code'),
                price=request.form.get('price'),
                color=request.form.get('color'),
                description=request.form.get('description'),
                made_of=request.form.get('made_of'),
            )
            db.session.add(new_good)
            db.session.commit()
            
        all_goods = db.session.execute(db.select(Good).order_by(Good.id.desc())).scalars().all()
        return render_template('admin.html', password=password, all_goods=all_goods)
    else: 
        return abort(403)

@app.route("/delete/<int:product_id>")
def delete_product(product_id):
    product_to_delete = db.session.execute(db.select(Good).where(Good.id == product_id)).scalar()
    db.session.delete(product_to_delete)
    db.session.commit()

    return redirect(url_for("admin", password="anjio09523ezsnjoky63dghqmqqplq7y1d435r11cv1"))
     
@app.route('/get_warehouses', methods = ["POST"])
def get_warehouses():
    dataFromPOST = request.get_json() 
    city_name = dataFromPOST.get("CityName", "Київ")
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

    payload = {
        "apiKey": API_KEY,
        "modelName": "AddressGeneral",
        "calledMethod": "getWarehouses",
        "methodProperties": {
                "FindByString" : InputByUser_House,
                "CityName" : nameCity,
                "CityRef" : "",
                "Page" : "",
                "Limit" : "150",
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
    
def send_telegram_message(order_data):
    goods_list = order_data.get('goodsToBuyTELEGRAM', [])
    total = 0
    for item in goods_list:
        total += int(item.get('price', 0).replace("₴", ""))
    formatted_goods = ""
    for index, item in enumerate(goods_list, start=1):
        formatted_goods += (
            f"      📦 Товар {index}:\n"
            f"              Назва: {item.get('name', 'Невідомо')}\n"
            f"              Код: {item.get('code', 'Невідомо')}\n"
            f"              Розмір: {item.get('size', 'Невідомо')}\n"
            f"              Колір: {item.get('color', 'Невідомо')}\n"
            f"              Ціна: {item.get('price', 'Невідомо')}\n\n"
        )
    message = (
        f"🛒 НОВЕ ЗАМОВЛЕННЯ:\n\n"
        f"👤 Прізвище: {order_data.get('secondNameTELEGRAM', 'НеНадано, звертайтесь кудись))')}\n"
        f"👤 Ім'я: {order_data.get('nameTELEGRAM', 'НеНадано, звертайтесь кудись))')}\n"
        f"👤 По батькові: {order_data.get('fatherNameTELEGRAM', 'НеНадано, звертайтесь кудись))')}\n"
        f"📧 Електронна адреса: {order_data.get('emailTELEGRAM', 'НеНадано, звертайтесь кудись))')}\n"
        f"📞 Телефон: {order_data.get('phoneTELEGRAM', 'НеНадано, звертайтесь кудись))')}\n"
        f"💬 Коментар до замовлення: {order_data.get('commentTELEGRAM', 'НеНадано, звертайтесь кудись))')}\n"
        f"🌍 Область: {order_data.get('regionTELEGRAM', 'НеНадано, звертайтесь кудись))')}\n"
        f"🏙️ Місто: {order_data.get('cityTELEGRAM', 'НеНадано, звертайтесь кудись))')}\n"
        f"🏤 Відділення: {order_data.get('warehouseTELEGRAM', 'НеНадано, звертайтесь кудись))')}\n"
        f"💳 Оплата: {order_data.get('paymentMethodTELEGRAM', 'НеНадано, звертайтесь кудись))')}\n\n"
        f"🛍️ Товари:\n{formatted_goods}\n\n"
        f"💰 Кінцева сума: {total}"
    )

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message, "parse_mode": "Markdown"}

    response = requests.post(url, json=payload)
    if response.status_code != 200:
        print("Error sending message:", response.text)

    shop_list = [item.get('name') for item in goods_list]

    email = Email()
    email.send_email(order_data.get('emailTELEGRAM'), total, ', '.join(shop_list))
    return response.json()

@app.route("/new_order", methods=["POST"])
def new_order():
    try:
        order_data = request.json
        if not order_data:
            return jsonify({"status": "error", "message": "Invalid input data"}), 400

        print("Received order data:", order_data)
        response = send_telegram_message(order_data)
        print("Telegram API response:", response)
        return jsonify({"status": "success", "message": "Order sent to Telegram"})
    except Exception as e:
        print("Error:", str(e))
        return jsonify({"status": "error", "message": str(e)})
    
@app.route('/script/index.js')
def serve_script():
    return send_from_directory('script', 'index.js')


if __name__ == "__main__":
    app.run(debug=True, port=5000)

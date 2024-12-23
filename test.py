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

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_KEY')
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_URI")
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///merch.db"
db.init_app(app)
Bootstrap5(app)






url = "https://api.novaposhta.ua/v2.0/json/"
# payload = {
#    "apiKey": API_KEY,
#    "modelName": "AddressGeneral",
#    "calledMethod": "getSettlements",
#    "methodProperties": {
#         # "AreaRef" : "71508131-9b87-11de-822f-000c2965ae0e"
#         # "Ref" : "71508131-9b87-11de-822f-000c2965ae0e"
#         # "RegionRef" : "71508131-9b87-11de-822f-000c2965ae0e"
#     }
# }

payload = {
   "apiKey": API_KEY,
   "modelName": "AddressGeneral",
   "calledMethod": "getStreet",
   "methodProperties": {
"CityRef" : "db5c88f5-391c-11dd-90d9-001a92567626",
"FindByString" : "зам",
"Limit" : "100"
   }
}

# {
#    "apiKey": API_KEY,
#    "modelName": "AddressGeneral",
#    "calledMethod": "searchSettlementStreets",
#    "methodProperties": {
#         "StreetName" : "Бу",
#         "SettlementRef" : "e7157fcd-4b33-11e4-ab6d-005056801329"
#    }
# }

# {
#    "apiKey": API_KEY,
#    "modelName": "AddressGeneral",
#    "calledMethod": "searchSettlementStreets",
#    "methodProperties": {
#         "StreetName" : "Буськ",
#         "SettlementRef" : "e7157fcd-4b33-11e4-ab6d-005056801329"
#    }
# }



# {
#     "apiKey": API_KEY,
#     "modelName": "AddressGeneral",
#     "calledMethod": "getSettlements",
#     "methodProperties": {
#         "AreaRef": "dcaad8fb-4b33-11e4-ab6d-005056801329",
#         "Page": "1",
#         "Limit": "50"
#     }
# }

res = requests.get(url, json=payload)
res.raise_for_status()
res_data = res.json()
print(res_data)
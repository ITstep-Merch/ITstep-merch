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
   "calledMethod": "getCities",
   "methodProperties": {
        "Page" : "1",
        "FindByString" : "Буськ",
        "Limit" : "20"
    }
    }


res = requests.get(url, json=payload)
res.raise_for_status()
res_data = res.json()
print(res_data)
from flask import Blueprint, request, Response
from model import fb1qModel
import json
from coder import MyEncoder
from flask import app
from .util import ret

fb1qRec = Blueprint("4b1q", __name__, url_prefix="/4b1q")

@fb1qRec.route("/", methods=["POST"])

def fb1qinsert():
    content = request.json
    account = content['account']
    Tracecode = content['Tracecode']
    fb1q_type =content['fb1q_type']
    data = fb1qModel.insert(account,Tracecode,fb1q_type)
    return ret(data)
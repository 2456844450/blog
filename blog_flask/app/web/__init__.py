from flask import Blueprint

web = Blueprint('web', __name__)

from app.web import article
from app.web import timeaxis
from app.web import auth
from app.web import message

from app.web import comment
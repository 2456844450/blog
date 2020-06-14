from flask import request,jsonify,current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from app.models.user import User
import functools

def create_token(api_user):

    s = Serializer(current_app.config["SECRET_KEY"], expires_in=3600)
    token = s.dumps({"id": api_user}).decode("ascii")
    return token

def verify_token(token):

    s = Serializer(current_app.config["SECRET_KEY"])
    try:
        data = s.loads(token)
    except Exception:
        return None
    user = User.query.get(data['id'])
    return user

def login_required(view_func):
    @functools.wraps(view_func)
    def verify_token(*args,**kwargs):
        try:
            token = request.headers['Authorization']
        except Exception:
            return jsonify({'code' : 201,'msg' : '缺少参数token'})

        s = Serializer(current_app.config["SECRET_KEY"])
        try:
            s.loads(token)
        except Exception:
            return jsonify({'code' : 201,'msg' : '登录已过期'})

        return view_func(*args,**kwargs)
    return verify_token
from flask import request,jsonify

from app.models.base import db
from app.models.message import Message
from . import web

@web.route('/api/addMessage', methods=['POST'])
def addMessage():
    form = request.json
    if request.method == 'POST':
        with db.auto_commit():
            message = Message()
            message.set_attrs(form)
            db.session.add(message)

        return jsonify({
            'code': 0,
            'message': '留言成功'
        })
    return jsonify({
        'code': 0,
        'message': '操作不当'
    })
from flask import request,jsonify

from app.models.article import Article

from sqlalchemy import desc


from app import create_app
from app.models.base import db
from app.models.timeaxis import Timeaxis

from . import web
from datetime import datetime


@web.route('/api/timeaxis/addTimeAxis', methods=['POST'])
def addTimeAxis():

    form = request.form

    if request.method == 'POST':
        with db.auto_commit():
            timeaxis = Timeaxis()
            timeaxis.set_attrs(form)
            db.session.add(timeaxis)


        return jsonify({
            'code': 200,
            'message': '添加历程成功'
        })
    return jsonify({
        'code': 200,
        'message': '小可爱别瞎玩哦~'
    })

@web.route('/api/getTimeAxisList', methods=['GET'])
def getTimeAxisList():
    keyword = request.args.get('keyword')
    pageNum = request.args.get('pageNum')
    pageSize = request.args.get('pageSize')

    if pageNum is not None:
        pageNum = int(pageNum)
    if pageSize is not None:
        pageSize = int(pageSize)
    timeaxis = Timeaxis.query.filter_by(state=1).order_by(desc(Timeaxis.create_time)).all()

    list = []
    for time in timeaxis:
        state = time.state
        _id = time.id
        title = time.title
        content = time.content
        start_time = time.start_time
        end_time = time.end_time
        list.append({
            'state': state,
            '_id': _id,
            'title': title,
            'content': content,
            'start_time': start_time,
            'end_time': end_time
        })
    return jsonify({
        'code': 0,
        'message': '请求文章列表成功',
        'data': {
            'list': list,
            'count': 100
        }

    })


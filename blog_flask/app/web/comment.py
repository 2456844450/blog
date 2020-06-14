
from flask import request,jsonify

from app.models.article import Article
from app.models.comment import Comment
from app.models.user import User
from app.models.base import db


from sqlalchemy import desc

from sqlalchemy import func
from app import create_app
from . import web
from datetime import datetime
app = create_app()


@web.route('/api/addThirdComment', methods=['POST'])
def addThirdComment():
    form = request.json
    comment_id = form['comment_id']
    comment_id = int(comment_id)
    #文章的id
    article_id = form['article_id']
    #评论用户的id
    user_id = form['user_id']
    #对谁评论的id
    to_user = form['to_user']
    to_user = int(to_user)
    content = form['content']
    with db.auto_commit():
        comment = Comment()
        comment.article_id = article_id
        comment.article_type = 1
        comment.from_uid = user_id
        comment.to_uid = to_user
        comment.origin_uid = to_user
        comment.content = content
        comment.comment_id = comment_id
        db.session.add(comment)
        article = Article.query.filter_by(id=article_id).first()
        article.comments +=1
    return jsonify({
        'code': 0,
        'message': '二级评论成功'
    })

@web.route('/api/addComment', methods=['POST'])
def addComment():

    form = request.json
    article_id = form.get('article_id')
    user_id = form.get('user_id')
    content = form.get('content')
    article = Article.query.filter_by(id=article_id).first()
    user = User.query.filter_by(id=user_id).first()
    if article and user:
        with db.auto_commit():
            article.comments +=1
            comment = Comment()
            comment.article_id = article_id
            comment.content = content
            comment.from_uid = user_id
            db.session.add(comment)
        return jsonify({
            'code': 0,
            'message':'评论成功'
        })
    return jsonify({
        'code': 1,
        'message': '评论失败'
    })
from app import app, db
from app.models import Posts
from flask import request, jsonify, make_response
import json

@app.route("/", methods=["GET","POST"])
def home():
    data = {
        'message': 'Hello World!',
        'status': 200
    }
    return make_response(jsonify(data))


@app.route("/posts/list", methods=["GET"])
def getPosts():
    postList = Posts.query.all()
    postObject = [{'id': post.id, 'title': post.title, 'description': post.description} for post in postList]

    data = {
        'status': 200,
        'result': postObject
    }
    return make_response(jsonify(data))

@app.route("/posts/list/<int:id>", methods=["GET"])
def getPostById(id):
    post = Posts.query.get(id)
    if(post):
        data = {
            'message': 'Post Info!',
            'status': 200,
            'data': {
                'id': post.id,
                'title': post.title,
                'description': post.description
            }
        }
    else:
        data = {
            'message': 'Invalid Post ID!',
            'status': 200
        }
    return make_response(jsonify(data))

@app.route("/posts/add", methods=["POST"])
def create_post():
    title = request.json['title']
    description = request.json['description']

    new_post = Posts(title, description)
    db.session.add(new_post)
    db.session.commit()

    data = {
        'message': 'New Post Created!',
        'status': 201
    }
    return make_response(jsonify(data))


@app.route("/posts/update", methods=["POST"])
def update_post():
    id = request.json['id']
    title = request.json['title']
    description = request.json['description']

    post = Posts.query.get(id)
    if(post):
        post.title = title
        post.description = description
        db.session.commit()

        data = {
            'message': 'Post has been updated.',
            'status': 201
        }
    else:
        data = {
            'message': 'Post does not exist',
            'status': 200
        }
    return make_response(jsonify(data))
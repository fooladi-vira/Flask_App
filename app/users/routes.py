from flask import Blueprint

blueprint=Blueprint('users',__name__)

@blueprint.route('/reg')
def login():
    return 'hello'
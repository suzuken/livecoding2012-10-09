#!/usr/bin/env python

from flask import Flask
from mongokit import Connection, Document

DEBUG = True

# configuration
MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017

app = Flask(__name__)
app.config.from_object(__name__)

connection = Connection(
        app.config['MONGODB_HOST'],
        app.config['MONGODB_PORT']
        )

class Post(object):
    structure = {
        'name': unicode,
        'email': unicode,
    }
    validators = {
        'name': max_length(50),
        'email': max_length(120)
    }
    use_dot_notation = True
    def __repr__(self):
        return '<User %r>' % (self.name)

@app.route('/')
def index():
    return "hello"

if __name__ == '__main__':
    app.run()

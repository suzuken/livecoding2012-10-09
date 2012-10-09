#!/usr/bin/env python

from flask import Flask, render_template, redirect, url_for
from mongokit import Connection, Document
import datetime

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

class Entry(object):
    structure = {
        'title': unicode,
        'body': unicode,
        'author': unicode,
        'datetime': basestring,
    }

@app.route('/')
def index():
    # return "hello"
    collection = connection['test'].entry
    entries = collection.find()
    # TODO: retrieve from db
    # entries = [entry]

    return render_template("top.html", entries=entries)

@app.route('/add_entry')
def add_example():
    collection = connection['test'].entry
    entry = {
        'title': 1,
        'body': 2,
        'author': 3,
        'datetime': 3
            }
    collection.insert(entry)
    return redirect(url_for("index"))

@app.route('/login')
def login():
    pass

@app.route('/show_entries')
def show_boards():
    pass

if __name__ == '__main__':
    app.run()

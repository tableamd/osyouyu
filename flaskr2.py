# all the imports
#coding:utf-8
from __future__ import with_statement
from flask import Flask, request, session, g, redirect, url_for
from flask import abort, render_template, flash
from webbrowser import open

# configuration
#DATABASE = 'flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'

app = Flask(__name__)
app.config.from_object(__name__)

counter = 0
all_counter = 0


@app.route('/')
def show_entries():
    return render_template('startpage.html')


@app.route('/osyoyu')
def osyoyu():
    global counter
    global all_counter
    return render_template("untitled.html",couter=counter,all_counter=all_counter)


@app.route('/add', methods=['POST'])
def add_entry():
    hoge = False
    global counter
    global all_counter

    counter += 1
    all_counter += 1

    if counter == 100:
        counter = 0
        hoge = True
        #GPIO関係の命令をここに書く？
    else:
        hoge*=0

    return render_template("untitled.html", counter=str(counter), all_counter=all_counter,hoge=hoge)


if __name__ == "__main__":
    app.run()
   #open("http://127.0.0.1:5000")

"""
Домашнее задание №5
Первое веб-приложение

создайте базовое приложение на Flask
создайте index views /
добавьте страницу /about/, добавьте туда текст
создайте базовый шаблон (используйте https://getbootstrap.com/docs/5.0/getting-started/introduction/#starter-template)
в базовый шаблон подключите статику Bootstrap 5 и добавьте стили, примените их (!!!)
в базовый шаблон добавьте навигационную панель nav (https://getbootstrap.com/docs/5.0/components/navbar/)
в навигационную панель добавьте ссылки на главную страницу / и на страницу /about/ при помощи url_for
"""
from flask import Flask
from flask import Blueprint, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("home.html", text="Hello, World!")

@app.route("/about/")
def about():
    return render_template("./about.html", text="This page had been made with Python")

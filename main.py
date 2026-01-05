"""
Flask-приложение с использованием Bootstrap и Jinja2.

Создаёт простое веб-приложение с базовым шаблоном
и двумя страницами: главная и о нас.
"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    """Главная страница приложения."""
    return render_template('home.html')


@app.route('/about')
def about():
    """Страница "О нас"."""
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)


import logging
from json import JSONDecodeError

from flask import Blueprint, render_template, request

from functions import save_picture, func_add_post

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates_name')


@loader_blueprint.route('/post')
def add_post_page():
    """Страница добавленных постов"""
    return render_template('post_form.html')


@loader_blueprint.route('/post', methods=['POST'])
def add_post():
    """Страница добавления постов"""
    picture = request.files.get('picture')
    content = request.form.get('content')

    ALLOWED_EXTENSIONS = {'png', 'jpeg'}
    filename = picture.filename
    extension = filename.split(".")[-1]
    if extension not in ALLOWED_EXTENSIONS:
        picture.save(f"./uploads/images/{filename}")
        logging.info('Загруженный файл не поддерживается')
        return f"Тип файлов {extension} не поддерживается"
    if not picture or not content:
        return "Нет картинки и/или текста"
    try:
        picture_path: str = '/' + save_picture(picture)
    except JSONDecodeError:
        return 'Невалидный файл'
    except FileNotFoundError:
        logging.info('Файл не найден')
        return 'Файл не найден'
    post: dict = func_add_post({'pic': picture_path, 'content': content})

    return render_template('post_uploaded.html', post=post)

from json import JSONDecodeError

from flask import Blueprint, render_template, request

from functions import get_posts_by_words

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates_name')


@main_blueprint.route('/')
def main_page():
    """Главная страница"""
    return render_template('index.html')


@main_blueprint.route('/search/')
def search_page():
    """Страница поиска по слову"""
    search_query = request.args.get('s', '')
    try:
        posts = get_posts_by_words(search_query)
    except FileNotFoundError:
        # logging.info('Файл не найден')
        return 'Файл не найден'
    except JSONDecodeError:
        return 'Невалидный файл'

    return render_template('post_list.html', query=search_query, posts=posts)


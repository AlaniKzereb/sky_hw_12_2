import json

from flask import request

POSTS_PATH = 'posts.json'

def load_posts():
    """
    Чтение данных из JSON файла
    Args: POSTS_PATH: имя файла
    Returns: декодировнные данные
    """
    with open(POSTS_PATH, 'r', encoding='utf-8') as file:
        return json.load(file)

def get_posts_by_words(word):
    """Поиск постов по слову
    Returns: список постов """
    result = []
    for post in load_posts():
        if word.lower() in post['content'].lower():
            result.append(post)
    return result

def save_picture(picture):
    """Сохраняет картинку из формируемого поста
    Returns: путь к картинке"""
    filename = picture.filename
    path = f'./uploads/images/{filename}'
    picture.save(path)
    return path


def func_add_post(post: dict) -> dict:
    """Добавляет новый пост в имеющийся файл джейсон-типа
    Returns: новый пост"""
    posts = load_posts()
    posts.append(post)
    with open(POSTS_PATH, 'w', encoding='utf-8') as file:
        json.dump(posts, file)
    return post

import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_posts():
    # Получение списка постов
    url = f"{BASE_URL}/posts"
    response = requests.get(url)

    assert response.status_code == 200, "Не удалось получить посты"
    assert len(response.json()) > 0, "Не удалось получить посты"

def test_get_posts_with_parameters():
    # Получение списка постов определенного пользователя
    url = f"{BASE_URL}/posts"
    params = {"userId": 1}
    response = requests.get(url, params=params)

    assert response.status_code == 200, "Не удалось получить посты"
    assert len(response.json()) > 0, "Не удалось получить посты"
    for post in response.json():
        assert post["userId"] == 1, f"Пост '{post}' принадлежит другому пользователю"

def test_get_single_post():
    # Получение одного поста
    post_id = 1
    url = f"{BASE_URL}/posts/{post_id}"
    response = requests.get(url)

    assert response.status_code == 200, "Не удалось получить пост"
    assert response.json()["id"] == post_id, "Не удалось получить пост"

def test_create_new_post():
    # Добавление нового поста
    url = f"{BASE_URL}/posts"
    data = {
        "title": "Новый пост",
        "body": "Это новый пост",
        "userId": 1,
    }
    response = requests.post(url, json=data)

    assert response.status_code == 201, "Не удалось создать пост"
    assert response.json()["title"] == "Новый пост", "Не удалось создать пост"


def test_delete_post():
    # Удаление поста
    url = f"{BASE_URL}/posts"
    data = {
        "title": "Пост для удаления",
        "body": "Это новый пост",
        "userId": 1,
    }
    create_response = requests.post(url, json=data)
    created_post_id = create_response.json()["id"]

    delete_url = f"{url}/{created_post_id}"
    delete_response = requests.delete(delete_url)

    assert delete_response.status_code == 200, "Не удалось удалить пост"
    assert delete_response.json() == {}, "Не удалось удалить пост"

    get_response = requests.get(delete_url)
    assert get_response.status_code == 404, "Пост все еще существует после удаления"

@pytest.mark.parametrize("test_function", [
    test_get_posts,
    test_get_posts_with_parameters,
    test_get_single_post,
    test_create_new_post,
    test_delete_post
])
def test_api_endpoints(test_function):
    test_function()
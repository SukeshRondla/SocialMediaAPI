import pytest
from app import schemas

# Assuming you have fixtures for authorized_client, client, test_posts, and test_user

def test_get_all_posts(authorized_client, test_posts):
    response = authorized_client.get("/posts/")
    assert response.status_code == 200
    assert len(response.json()) == len(test_posts)

def test_unauthorized_user_get_all_posts(client):
    response = client.get("/posts/")
    assert response.status_code == 401

def test_get_one_post(authorized_client, test_posts):
    post_id = test_posts[0].id
    response = authorized_client.get(f"/posts/{post_id}")
    assert response.status_code == 200
    assert response.json()["title"] == test_posts[0].title
    assert response.json()["content"] == test_posts[0].content

def test_create_post(authorized_client, test_user):
    data = {
        "title": "New Post",
        "content": "This is the content",
        "published": True
    }
    response = authorized_client.post("/posts/", json=data)
    assert response.status_code == 201
    created_post = response.json()
    assert created_post["title"] == data["title"]
    assert created_post["content"] == data["content"]
    assert created_post["published"] == data["published"]
    assert created_post["owner_id"] == test_user['id']

# Add similar tests for unauthorized_user_create_post, test_create_post_default_published_true, and other cases.

def test_delete_post_success(authorized_client, test_posts):
    post_id = test_posts[0].id
    response = authorized_client.delete(f"/posts/{post_id}")
    assert response.status_code == 204

# Add tests for delete_post_non_exist, delete_other_user_post, and other cases.

def test_update_post(authorized_client, test_posts):
    post_id = test_posts[0].id
    data = {
        "title": "Updated Title",
        "content": "Updated Content",
    }
    response = authorized_client.put(f"/posts/{post_id}", json=data)
    assert response.status_code == 200
    updated_post = response.json()
    assert updated_post["title"] == data["title"]
    assert updated_post["content"] == data["content"]

# Add tests for update_other_user_post, unauthorized_user_update_post, and update_post_non_exist.

def test_unauthorized_user_get_one_post(client, test_posts):
    post_id = test_posts[0].id
    response = client.get(f"/posts/{post_id}")
    assert response.status_code == 401

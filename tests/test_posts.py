import pytest
from app import schemas

@pytest.fixture
def post_data():
    return {
        "title": "New Post",
        "content": "This is the content",
        "published": True
    }

@pytest.fixture
def existing_post(authorized_client, post_data):
    response = authorized_client.post("/posts/", json=post_data)
    return response.json()

@pytest.fixture
def test_post(authorized_client, existing_post):
    return existing_post

class TestPostEndpoints:

    def test_get_all_posts(self, authorized_client, test_posts):
        response = authorized_client.get("/posts/")
        assert response.status_code == 200
        assert len(response.json()) == len(test_posts)

    def test_unauthorized_user_get_all_posts(self, client):
        response = client.get("/posts/")
        assert response.status_code == 401

    def test_get_one_post(self, authorized_client, test_post):
        post_id = test_post["id"]
        response = authorized_client.get(f"/posts/{post_id}")
        assert response.status_code == 200
        assert response.json()["title"] == test_post["title"]
        assert response.json()["content"] == test_post["content"]

    def test_create_post(self, authorized_client, test_user, post_data):
        response = authorized_client.post("/posts/", json=post_data)
        assert response.status_code == 201
        created_post = response.json()
        assert created_post["title"] == post_data["title"]
        assert created_post["content"] == post_data["content"]
        assert created_post["published"] == post_data["published"]
        assert created_post["owner_id"] == test_user['id']

    # Add similar tests for unauthorized_user_create_post, test_create_post_default_published_true, and other cases.

    def test_delete_post_success(self, authorized_client, test_post):
        post_id = test_post["id"]
        response = authorized_client.delete(f"/posts/{post_id}")
        assert response.status_code == 204

    # Add tests for delete_post_non_exist, delete_other_user_post, and other cases.

    def test_update_post(self, authorized_client, test_post):
        post_id = test_post["id"]
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

    def test_unauthorized_user_get_one_post(self, client, test_post):
        post_id = test_post["id"]
        response = client.get(f"/posts/{post_id}")
        assert response.status_code == 401

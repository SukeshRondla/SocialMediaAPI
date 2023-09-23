import pytest
from app import models

# Define a fixture for creating a vote
@pytest.fixture()
def test_vote(session, test_posts, test_user):
    new_vote = models.Vote(post_id=test_posts[3].id, user_id=test_user['id'])
    session.add(new_vote)
    session.commit()

# Group related test cases with docstrings
class TestVoteEndpoints:
    def test_vote_on_post(self, authorized_client, test_posts):
        """Test voting on a post."""
        res = authorized_client.post("/vote/", json={"post_id": test_posts[3].id, "dir": 1})
        assert res.status_code == 201

    def test_vote_twice_post(self, authorized_client, test_posts, test_vote):
        """Test attempting to vote on the same post twice."""
        res = authorized_client.post("/vote/", json={"post_id": test_posts[3].id, "dir": 1})
        assert res.status_code == 409

    def test_delete_vote(self, authorized_client, test_posts, test_vote):
        """Test deleting a vote on a post."""
        res = authorized_client.post("/vote/", json={"post_id": test_posts[3].id, "dir": 0})
        assert res.status_code == 201

    def test_delete_vote_non_exist(self, authorized_client, test_posts):
        """Test deleting a non-existent vote."""
        res = authorized_client.post("/vote/", json={"post_id": test_posts[3].id, "dir": 0})
        assert res.status_code == 404

    def test_vote_post_non_exist(self, authorized_client, test_posts):
        """Test voting on a non-existent post."""
        res = authorized_client.post("/vote/", json={"post_id": 80000, "dir": 1})
        assert res.status_code == 404

    def test_vote_unauthorized_user(self, client, test_posts):
        """Test voting as an unauthorized user."""
        res = client.post("/vote/", json={"post_id": test_posts[3].id, "dir": 1})
        assert res.status_code == 401

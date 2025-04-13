from flask import url_for
import pytest
from talenthawk.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Test that the home page loads"""
    response = client.get('/')
    assert response.status_code == 200

def test_player_detail(client):
    """Test that player detail page loads"""
    response = client.get('/player/1')
    assert response.status_code == 200

def test_comparison_page(client):
    """Test that comparison page loads"""
    response = client.get('/comparison')
    assert response.status_code == 200

def test_analytics_page(client):
    """Test that analytics page loads"""
    response = client.get('/analytics')
    assert response.status_code == 200 
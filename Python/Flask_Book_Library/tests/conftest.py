import pytest
import os
from project import app, db


@pytest.fixture(scope='function')
def test_app():
    """Create application for testing"""
    # Use in-memory SQLite database for testing
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['WTF_CSRF_ENABLED'] = False
    
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()


@pytest.fixture(scope='function')
def test_db(test_app):
    """Create database for testing"""
    return db


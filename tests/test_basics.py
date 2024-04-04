import unittest
from app import create_app, db
from flask import current_app
from app.models import Role, User


class Basic_Test_Case(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])

    def test_add_to_database(self):
        role_admin = Role(role_name="Admin", id=1)
        user = User(name="johnny", role=role_admin)
        db.session.add_all([role_admin, user])
        db.session.commit()
        user = User.query.filter_by(name="johnny").first()
        self.assertFalse(user is None)

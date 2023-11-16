import os
from unittest import TestCase

from models import db, User, Recipe

os.environ['DATABASE_URL'] = "postgresql:///recipestest"

from app import app

db.drop_all()
db.create_all()

class UserModelTestCase(TestCase):
    """Test user model."""

    def setUp(self):
        """Create test client."""

        User.query.delete()
        Recipe.query.delete()

        self.client = app.test_client()


    def test_user_model(self):
        """Does basic user model work?"""

        u = User(
            username="testuser",
            email="test@test.com",
            password="HASHED_PASSWORD",
            diet='none',
            allergies=None
        )

        db.session.add(u)
        db.session.commit()

        # user should have no saved recipes
        self.assertEqual(len(u.recipes), 0)

        # test repr method
        self.assertIn(u.username, repr(u))


    def test_user_recipes(self):
        """Can recipes be added/removed from user?"""

        u = User(
            username="testuser",
            email="test@test.com",
            password="HASHED_PASSWORD",
            diet='none',
            allergies=None
        )

        db.session.add(u)
        db.session.commit()

        r = Recipe(
            api_id=1,
            title="test",
            user_id=u.id
        )

        db.session.add(r)
        db.session.commit()

        self.assertEqual(len(u.recipes), 1)

        # test is_saved method
        self.assertTrue(u.is_saved(r))
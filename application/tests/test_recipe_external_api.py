import os
from unittest import TestCase
import requests

from models import db, User, Recipe
from secret_keys import API_SECRET_KEY

os.environ['DATABASE_URL'] = "postgresql:///recipestest"

from app import app, CURR_USER_KEY, BASE_URL
db.create_all()
app.config['WTF_CSRF_ENABLED'] = False


class RecipeViewsTestCase(TestCase):
    """Test user views."""

    def setUp(self):
        """Create test client, add sample data."""

        User.query.delete()
        Recipe.query.delete()

        self.client = app.test_client()

        self.testuser = User.signup(username="testuser",
                                    email="test@test.com",
                                    password="testuser",
                                    image_url=None,
                                    diet='none',
                                    allergies=None)

        db.session.commit()
        

    def test_api_call_simple(self):
        """Does simple recipe search with only query work?"""

        d = {'query': 'pasta',
             'apiKey': API_SECRET_KEY}
        resp = requests.get(f"{BASE_URL}/complexSearch",
                               params=d)
        
        self.assertEqual(resp.status_code, 200)


    def test_api_call_advanced(self):
        """Does advanced recipe search with more arguments work?"""

        d = {'query': 'pasta',
             'ingredients': "tomato,cheese",
             'number': 1,
             'diet': 'vegetarian',
             'excludeIngredients': 'peanuts',
             'sort': 'min-missing-ingredients',
             "type": "main course",
             'apiKey': API_SECRET_KEY}
             
        resp = requests.get(f"{BASE_URL}/complexSearch",
                               params=d)
        
        self.assertEqual(resp.status_code, 200)
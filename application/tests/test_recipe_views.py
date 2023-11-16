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
    """Test recipe views."""

    def setUp(self):
        """Create test client, add sample data."""

        User.query.delete()
        Recipe.query.delete()

        self.client = app.test_client()
        self.maxDiff = None

        self.testuser = User.signup(username="testuser",
                                    email="test@test.com",
                                    password="testuser",
                                    image_url=None,
                                    diet='none',
                                    allergies=None)

        db.session.commit()


    ############################################################################
    # Testing basic recipe search
    def test_recipe_search_display(self):
        """Does basic recipe search on homepage display properly?"""

        resp = self.client.get('/')
        html = resp.get_data(as_text=True)
        self.assertIn("Find your new", html)


    def test_recipe_search_no_query(self):
        """Do results show up when query is empty?"""
        d = {'query': ''}
        resp = self.client.post('/', data=d, follow_redirects=True)
        self.assertEqual(resp.status_code, 200)

        html = resp.get_data(as_text=True)
        self.assertIn('Find your new', html)

        # make sure no results show up when user goes straight to results route
        resp = self.client.get('/recipes/results', follow_redirects=True)
        html = resp.get_data(as_text=True)
        self.assertIn("Find your new", html)


    def test_recipe_search(self):
        """Do results show up when user searches for a food?"""

        d = {'query': 'pasta'}
        resp = self.client.post('/', data=d, follow_redirects=True)
        self.assertEqual(resp.status_code, 200)

        html = resp.get_data(as_text=True)
        self.assertIn('Results for', html)


    def test_recipe_search_invalid(self):
        """Do results show up when query isn't food/drink?"""

        d = {'query': 'djfasldkfaj'}
        resp = self.client.post('/', data=d, follow_redirects=True)
        self.assertEqual(resp.status_code, 200)

        html = resp.get_data(as_text=True)
        self.assertIn('No recipes found', html)


    ############################################################################
    # Testing advanced recipe search
    
    def test_advanced_recipe_search_display(self):
        """Does advanced recipe search on homepage display properly?"""

        resp = self.client.get('/advanced-search')
        html = resp.get_data(as_text=True)
        self.assertIn("Advanced Search", html)


    def test_advanced_recipe_search_no_query(self):
        """Do results show up when user searches for nothing?"""

        d = {'query': '',
             'number': '1',
             'apiKey': API_SECRET_KEY}
        
        resp = self.client.post('/advanced-search', data=d, follow_redirects=True)
        self.assertEqual(resp.status_code, 200)

        html = resp.get_data(as_text=True)
        self.assertIn('Advanced Search', html)

    
    def test_advanced_recipe_search(self):
        """Do results show up when user searches for a food?"""
        
        d = {"query": "pasta",
             "includeIngredients": 'tomato',
             "number": 1,
             "diet": self.testuser.diet,
             "excludeIngredients": None,
             "sort": 'none',
             "sortDirection": 'asc',
             "type": 'none',
             "apiKey": API_SECRET_KEY}
            
        resp = self.client.post('/advanced-search', data=d, follow_redirects=True)
        self.assertEqual(resp.status_code, 200)

        html = resp.get_data(as_text=True)
        self.assertIn('Results for', html)


    def test_advanced_recipe_search_invalid(self):
        """Do results show up when query isn't food/drink?"""

        d = {"query": "sdlfkjasdlvkn",
             "includeIngredients": 'tomato',
             "number": 1,
             "diet": self.testuser.diet,
             "excludeIngredients": None,
             "sort": 'none',
             "sortDirection": 'asc',
             "type": 'none',
             "apiKey": API_SECRET_KEY}
        
        resp = self.client.post('/', data=d, follow_redirects=True)
        self.assertEqual(resp.status_code, 200)

        html = resp.get_data(as_text=True)
        self.assertIn('No recipes found', html)
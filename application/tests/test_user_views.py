import os
from unittest import TestCase
import requests

from models import db, User, Recipe
from secret_keys import API_SECRET_KEY

os.environ['DATABASE_URL'] = "postgresql:///recipestest"

from app import app, CURR_USER_KEY, BASE_URL
db.create_all()
app.config['WTF_CSRF_ENABLED'] = False


class UserViewsTestCase(TestCase):
    """Test user views."""

    def setUp(self):
        """Create test client, add sample data."""

        User.query.delete()
        Recipe.query.delete()

        self.client = app.test_client()
        self.maxDiff = None

        self.testuser = User.signup(username="testuser",
                                    email="test@test.com",
                                    password="testuser",
                                    image_url=User.image_url.default.arg,
                                    diet='none',
                                    allergies=None)

        db.session.commit()


    ############################################################################
    # Testing signup

    def test_user_signup_display(self):
        """Does signup form show up?"""

        resp = self.client.get('/signup')
        html = resp.get_data(as_text=True)

        self.assertEqual(resp.status_code, 200)
        self.assertIn('Save your recipes today', html)


    def test_user_signup_valid(self):
        """Can user sign up with valid credentials?"""

        d = {"username": "tester",
             "email": "tester@test.com",
             "password": "password01",
             "image_url": None,
             "diet": "none",
             "allergies": None}
        
        resp = self.client.post('/signup', data=d)
        self.assertEqual(resp.status_code, 302)

        user = User.query.filter_by(username='tester').one()
        self.assertEqual('tester', user.username)


    def test_user_signup_bad_password(self):
        """Can user sign up if password isn't long enough?"""

        d = {"username": "tester2",
             "email": "tester@test.com",
             "password": "hi",
             "image_url": None,
             "diet": "none",
             "allergies": None}
        
        resp = self.client.post('/signup', data=d)
        html = resp.get_data(as_text=True)
        self.assertIn('at least 8 characters', html)


    ############################################################################
    # Testing login

    def test_user_login_display(self):
        """Does login page properly show?"""

        resp = self.client.get('/login')
        html = resp.get_data(as_text=True)

        self.assertEqual(resp.status_code, 200)
        self.assertIn('Welcome back', html)


    def test_user_login_valid(self):
        """Can user log in with valid credentials?"""

        d = {"username": "testuser",
             "password": "testuser"}
        
        resp = self.client.post('/login', data=d, follow_redirects=True)
        html = resp.get_data(as_text=True)
        self.assertIn('Hello, testuser', html)
        

    def test_user_login_invalid_password(self):
        """Can user log in with invalid credentials?"""

        d = {"username": "testuser",
             "password": "testuser1"}
        
        resp = self.client.post('/login', data=d)
        html = resp.get_data(as_text=True)

        self.assertEqual(resp.status_code, 200)
        self.assertIn('Invalid credentials', html)


    ############################################################################
    # Testing updating profile

    def test_update_profile_display(self):
        """Does update form properly show?"""

        with self.client as c:
            with c.session_transaction() as sess:
                user_id = self.testuser.id
                sess[CURR_USER_KEY] = user_id

            resp = c.get(f"/users/{user_id}/update")
            self.assertEqual(resp.status_code, 200)

            html = resp.get_data(as_text=True)
            self.assertIn('Update profile', html)


    def test_update_profile_logged_in(self):
        """Can user update profile when logged in and with valid credentials?"""

        with self.client as c:
            with c.session_transaction() as sess:
                user_id = self.testuser.id
                sess[CURR_USER_KEY] = user_id

            d = {"username": "testuser",
                'email': "test@test.com",
                'password': "testuser",
                'image_url': None,
                'diet': 'none',
                'allergies': 'bananas'}
            resp = c.post(f"/users/{user_id}/update", data=d)
            self.assertEqual(resp.status_code, 302)
            html = resp.get_data(as_text=True)
            self.assertIn('Successfully updated profile', html)

    
    def test_update_profile_logged_in_invalid(self):
        """Can user update profile when logged in and with invalid credentials?"""

        with self.client as c:
            with c.session_transaction() as sess:
                user_id = self.testuser.id
                sess[CURR_USER_KEY] = user_id

            d = {"username": "testuser",
                'email': "test@test.com",
                'password': "testuser2",
                'image_url': None,
                'diet': 'none',
                'allergies': 'bananas'}
            resp = c.post(f"/users/{user_id}/update", data=d)
            self.assertEqual(resp.status_code, 302)


    ############################################################################
    # Testing updating profile

    def test_update_display_logged_out(self):
        """Does update form show when logged out?"""

        resp = self.client.get(f"/users/{self.testuser.id}/update")
        html = resp.get_data(as_text=True)
        self.assertIn('/login', html)


    def test_update_display_logged_in(self):
        """Does update form show when logged out?"""

        with self.client as c:
            with c.session_transaction() as sess:
                user_id = self.testuser.id
                sess[CURR_USER_KEY] = user_id

            resp = c.get(f"/users/{self.testuser.id}/update")
            html = resp.get_data(as_text=True)
            self.assertIn('Update profile', html)


    def test_update_profile_logged_out(self):
        """Can user update profile when logged out?"""

        resp = self.client.post(f"/users/{self.testuser.id}/update")
        html = resp.get_data(as_text=True)
        self.assertIn('/login', html)


    def test_update_profile_logged_in(self):
        """Can user update profile when logged in and with valid password?"""

        with self.client as c:
            with c.session_transaction() as sess:
                user_id = self.testuser.id
                sess[CURR_USER_KEY] = user_id

            d = {"username": "testuser",
                 "email": "test@test.com",
                 "password": "testuser",
                 "image_url": self.testuser.image_url,
                 "diet": 'vegetarian',
                 "allergies": 'bananas'}

            resp = self.client.post(f"/users/{self.testuser.id}/update", data=d, follow_redirects=True)
            html = resp.get_data(as_text=True)
            self.assertIn('Successfully updated profile', html)
            self.assertEqual(self.testuser.diet, 'vegetarian')


    def test_update_profile_logged_in_invalid(self):
        """Can user update profile when logged in and with invalid password?"""

        with self.client as c:
            with c.session_transaction() as sess:
                user_id = self.testuser.id
                sess[CURR_USER_KEY] = user_id

            d = {"username": "testuser",
                 "email": "test@test.com",
                 "password": "testuser1",
                 "image_url": self.testuser.image_url,
                 "diet": 'vegetarian',
                 "allergies": 'bananas'}

            resp = self.client.post(f"/users/{self.testuser.id}/update", data=d, follow_redirects=True)
            html = resp.get_data(as_text=True)
            self.assertIn('Invalid password', html)


    def test_update_profile_other_user(self):
        """Can user 1 update user 2's profile?"""

        d = {"username": "testuser2",
             "email": "test2@test.com",
             "password": "testuser2",
             "image_url": User.image_url.default.arg,
             "diet": 'none',
             "allergies": None}
        
        user2 = User.signup(**d)
        db.session.commit()

        self.assertEqual(len(User.query.all()), 2)

        resp = self.client.post('/login', 
                                data={"username": "testuser2",
                                      "password": "testuser2"},
                                follow_redirects=True)
        self.assertEqual(resp.status_code, 200)

        d = {"username": "testuser",
             "email": "test@test.com",
             "password": "testuser",
             "diet": 'vegan',
             "allergies": 'bananas'}

        resp = self.client.post(f"/users/{self.testuser.id}/update", data=d, follow_redirects=True)
        html = resp.get_data(as_text=True)
        self.assertIn("update your own", html)


    ############################################################################
    # Testing deleting profile

    def test_delete_profile_logged_out(self):
        """Can user delete profile when logged out?"""

        resp = self.client.post(f"/users/delete", follow_redirects=True)
        html = resp.get_data(as_text=True)
        self.assertIn('Find your new', html)


    def test_delete_profile_logged_in(self):
        """Can user update profile when logged in?"""

        with self.client as c:
            with c.session_transaction() as sess:
                user_id = self.testuser.id
                sess[CURR_USER_KEY] = user_id

            users = User.query.filter_by(id=self.testuser.id).all()
            self.assertEqual(len(users), 1)

            resp = self.client.post(f"/users/delete", follow_redirects=True)
            html = resp.get_data(as_text=True)
            self.assertIn('Successfully deleted profile', html)

            users = User.query.filter_by(id=self.testuser.id).all()
            self.assertEqual(len(users), 0)


    ############################################################################
    # Testing saving recipes

    def test_save_recipe_logged_in(self):
        """Can user save/unsave a recipe when logged in?"""

        self.assertEqual(len(self.testuser.recipes), 0)

        with self.client as c:
            with c.session_transaction() as sess:
                user_id = self.testuser.id
                sess[CURR_USER_KEY] = user_id

            resp = requests.get(f"{BASE_URL}/complexSearch",
                                params={"query": "pasta",
                                        "number": 1,
                                        "apiKey": API_SECRET_KEY})
            json = resp.json()
            recipe = json["results"][0]

            resp = c.post(f"/users/save_recipe/{recipe['id']}/user_detail",
                          follow_redirects=True)
            self.assertEqual(resp.status_code, 200)

            html = resp.get_data(as_text=True)

            self.assertIn('Recipe saved', html)
            self.assertEqual(len(self.testuser.recipes), 1)
            self.assertEqual(self.testuser.recipes[0].title, recipe["title"])

            resp = c.post(f"/users/unsave_recipe/{recipe['id']}/user_detail",
                          follow_redirects=True)
            self.assertEqual(resp.status_code, 200)

            html = resp.get_data(as_text=True)

            self.assertIn('Recipe unsaved', html)
            self.assertEqual(len(self.testuser.recipes), 0)


    def test_save_recipe_logged_out(self):
        """Can user save a recipe when logged out?"""

        arbitrary_api_id = 1

        resp = self.client.post(f"/users/save_recipe/{arbitrary_api_id}/home")
        self.assertEqual(resp.status_code, 302)

        html = resp.get_data(as_text=True)
        self.assertIn('/login', html)

    
    def test_unsave_recipe_logged_out(self):
        """Can user unsave a recipe when logged out?"""

        arbitrary_api_id = 1

        resp = self.client.post(f"/users/unsave_recipe/{arbitrary_api_id}/home")
        self.assertEqual(resp.status_code, 302)

        html = resp.get_data(as_text=True)
        self.assertIn('/login', html)     
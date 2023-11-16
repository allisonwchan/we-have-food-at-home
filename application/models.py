from datetime import datetime

from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

bcrypt = Bcrypt()
db = SQLAlchemy()

DEFAULT_IMAGE_URL = "https://tse1.explicit.bing.net/th?id=OIP.GHGGLYe7gDfZUzF_tElxiQHaHa&pid=Api&P=0&h=220"

class User(db.Model):
    """User in the system."""

    __tablename__ = 'users'

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    email = db.Column(
        db.Text,
        nullable=False,
        unique=True,
    )

    username = db.Column(
        db.Text,
        nullable=False,
        unique=True,
    )

    image_url = db.Column(
        db.Text,
        default=DEFAULT_IMAGE_URL
    )

    password = db.Column(
        db.Text,
        nullable=False,
    )

    diet = db.Column(
        db.Text
    )

    allergies = db.Column(
        db.Text,
        default=None
    )

    recipes = db.relationship('Recipe', backref='users', lazy=True)

    def __repr__(self):
        return f"<User #{self.id}: {self.username}, {self.email}>"

    @classmethod
    def signup(cls, username, email, password, image_url, diet, allergies):
        """Sign up user.

        Hashes password and adds user to system.
        """

        hashed_pwd = bcrypt.generate_password_hash(password).decode('UTF-8')

        user = User(
            username=username,
            email=email,
            password=hashed_pwd,
            image_url=image_url,
            diet=diet,
            allergies=allergies
        )

        db.session.add(user)
        return user

    @classmethod
    def authenticate(cls, username, password):
        """Find user with `username` and `password`.

        This is a class method (call it on the class, not an individual user.)
        It searches for a user whose password hash matches this password
        and, if it finds such a user, returns that user object.

        If can't find matching user (or if password is wrong), returns False.
        """

        user = cls.query.filter_by(username=username).first()

        if user:
            is_auth = bcrypt.check_password_hash(user.password, password)
            if is_auth:
                return user

        return False
    
    def is_saved(self, other_recipe):
        """Is recipe saved by user?"""

        found_recipe_list = [recipe for recipe in self.recipes if recipe == other_recipe]
        return len(found_recipe_list) == 1


class Recipe(db.Model):
    """Recipe model."""

    __tablename__ = 'recipes'
    
    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    api_id = db.Column(
        db.Integer,
        nullable=False
    )

    title = db.Column(
        db.Text,
        nullable=False
    )

    image = db.Column(
        db.Text
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id', ondelete='cascade'),
        nullable=False
    )

def connect_db(app):
    """Connect this database to provided Flask app."""

    db.app = app
    db.init_app(app)
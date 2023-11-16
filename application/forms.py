from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SelectField, IntegerField
from wtforms.validators import DataRequired, Email, Length, URL, NumberRange


diet_choices = [('none', 'None'),
                ('gluten-free', 'Gluten-free'), 
                ('ketogenic', 'Ketogenic'),
                ('vegetarian', 'Vegetarian'),
                ('lacto-vegetarian', 'Lacto-Vegetarian'),
                ('vegan', 'Vegan'),
                ('pescetarian', 'Pescetarian'),
                ('paleo', 'Paleo'),
                ('primal', 'Primal'),
                ('low-foodmap', 'Low-Foodmap'),
                ('whole30', 'Whole30')]

sort_choices = [('none', 'None'),
                ('min-missing-ingredients', 'Number of missing ingredients'),
                ('calories', 'Calories'),
                ('time', 'Cooking time')]

sort_directions = [('none', 'None'),
                   ('asc', 'Ascending'),
                   ('desc', 'Descending')]

meal_choices = [('none', 'None'),
                ('main-course', 'Main course'),
                ('side-dish', 'Side dish'),
                ('dessert', 'Dessert'),
                ('drink', 'Drink')]


class UserAddForm(FlaskForm):
    """Form for adding users."""

    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[Length(min=8)])
    image_url = StringField('(Optional) Image URL')
    diet = SelectField('(Optional) Diet', choices=diet_choices)
    allergies = TextAreaField('(Optional) Allergies')


class UserUpdateForm(FlaskForm):
    """Form for updating user info."""

    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    image_url = StringField('(Optional) Image URL', validators=[URL()])
    diet = SelectField('(Optional) Diet', choices=diet_choices)
    allergies = TextAreaField('(Optional) Allergies')

    # just check that input password matches current password
    password = PasswordField('Password', validators=[DataRequired()])


class LoginForm(FlaskForm):
    """Login form."""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[Length(min=8)])


class SearchForm(FlaskForm):
    """Basic recipe search bar."""

    query = StringField('What are you craving today? (Such as pasta, rice, etc.)', validators=[DataRequired()])
    

class AdvancedSearchForm(FlaskForm):
    """Form for advanced search of recipes.
    Variable names correspond to the names used in the API."""

    query = StringField('What are you craving today? (Such as pasta, rice, etc.)', validators=[DataRequired()])
    includeIngredients = TextAreaField('What ingredients do you have?', validators=[DataRequired()])
    number = IntegerField('How many recipes?', validators=[NumberRange(min=1, max=100)])
    diet = SelectField('Any dietary restrictions?', choices=diet_choices)
    excludeIngredients = TextAreaField('(Optional) Any ingredients to exclude, like allergies?')
    sort = SelectField('(Optional) How should recipes be sorted?', choices=sort_choices)
    sortDirection = SelectField('(Optional) Sort in ascending or descending order?', choices=sort_directions)
    type = SelectField('(Optional) What kind of meal?', choices=meal_choices)
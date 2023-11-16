# WFH (We have Food at Home!)

*Reduce food waste and do more home cooking by finding recipes based on ingredients you have!*

[Deployed using Render!](https://we-have-food-at-home.onrender.com/)

### Features
**A logged out user can:**
- Search for recipes of a food/drink (for example, pasta)
  - This allows a user to just do a quick search for a general set of recipes.
- Do an *Advanced Search* to filter recipes based on what ingredients they have and other choices, such as number of results to return, dietary restrictions, and any ingredients to exclude
  - This allows a user to get more refined and specific results based on their needs.
- Signup for an account 
  - See what a user with an account can do below!

**A logged in user can:**
- Do everything an anonymous user can
- Signup with their dietary restrictions and allergies, which will automatically be applied when they do an Advanced Search
  - This way, a user doesn't have to repeatedly enter their diet/allergies when searching for recipes.
- Save recipes
  - If a user finds an interesting recipe, they can have it saved for future reference when they decide to cook it.
- Update/delete their own profile
  - A user's personal information or diet/allergies may change, so it's a good idea for the user to be able to change their own profile. They can also delete their own profile if they decide they want to terminate their account.

### User Flow
For both a logged out and logged in user, the landing page shows a search bar where a user can do a basic search for a food/drink and get recipes. There are also a few recommended recipes under the search bar. If the user is logged in, those recommended recipes will be filtered based on the user's diet and allergies (ex: if the user is vegetarian and allergic to peanuts, the recommended recipes will also be vegetarian and exclude peanuts).

Under the search bar, there is a link to the *Advanced Search*. Both a logged out and logged in user can access it. Here, a user can filter their recipe search based on more parameters, including number of results to return, what ingredients to include, and what kind of the meal the recipe is (such as main or side dish).

When a user searches for recipes and gets results, they can click on a recipe to see more details about it, such as a full list of ingredients, cooking time, and a link to the recipe source. If a user is logged in, they are able to save recipes by clicking the Bookmark symbol. If not logged in, a user will be redirected to login.

A user can view their saved recipes by clicking on their profile picture in the navbar (which only shows up if a user is logged in), clicking on "Profile", and navigating to the "Saved recipes" tab in their profile page. There is also a "Profile" tab, where a user can view their own information and also update or delete their profile.

In the navbar, there are 3 options for a logged in and logged out user: "WFH!", "About", and "Users". Clicking on "WFH!" redirects to the homepage, "About" to a page with a summary of what website provides, and "Users" to a list of all users. A user can view other users' profiles, although they can only view other users' saved recipes. 

Finally, a user can logout by clicking on their profile picture in the navbar and then clicking "Logout".

### API
WFH! is powered by the [Spoonacular](https://spoonacular.com/food-api/docs) API.

### Tech Stack
For the frontend, WFH! uses HTML, CSS, and JavaScript and is styled using the Minty theme from Bootswatch. The backend is powered with Python, Flask, SQLAlchemy, WTForms, and PostgreSQL.

### Important Note
WFH! can only handle 150 API calls per day, as detailed by the Spoontacular API free plan. If there are no results being returned despite entering a valid food or drink, it could be that WFH! has exceeded the daily limit of API calls. If that's the case, please try searching for recipes the next day!
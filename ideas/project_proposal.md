# Project Proposal

Use this template to help get you started right away! Once the proposal is complete, please let your mentor know that this is ready to be reviewed.

## Get Started

|            | Description                                                                                                                                                                                                                                                                                                                                              | Fill in |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| Tech Stack | What tech stack will you use for your final project? It is recommended to use the following technologies in this project: Python/Flask, PostgreSQL, SQLAlchemy, Heroku, Jinja, RESTful APIs, JavaScript, HTML, CSS. Depending on your idea, you might end up using WTForms and other technologies discussed in the course.                               | Flask, PostgreSQL, SQLAlchemy, WTForms, Jinja, Javascript, HTML, CSS |
| Type       | Will this be a website? A mobile app? Something else?                                                                                                                                                                                                                                                                                                    | Website |
| Goal       | What goal will your project be designed to achieve?                                                                                                                                                                                                                                                                                                      | Allow users to find recipes based on what ingredients they have, along with numerous filters on recipes based on dietary needs (ingredients to exclude, amounts of different nutrients, types of food like main meal or snack, etc.). Results will include the name of the recipe, a link to the recipe, and ingredients. |
| Users      | What kind of users will visit your app? In other words, what is the demographic of your users?                                                                                                                                                                                                                                                           | Anyone who has access to a kitchen and grocery store and wants to do more cooking and reduce food waste |
| Data       | What data do you plan on using? How are you planning on collecting your data? You may have not picked your actual API yet, which is fine, just outline what kind of data you would like it to contain. You are welcome to create your own API and populate it with data. If you are using a Python/Flask stack, you are required to create your own API. | [Spoonacular](https://spoonacular.com/food-api/docs) |

# Breaking down your project

When planning your project, break down your project into smaller tasks, knowing that you may not know everything in advance and that these details might change later. Some common tasks might include:

- Determining the database schema
- Sourcing your data
- Determining user flow(s)
- Setting up the backend and database
- Setting up the frontend
- What functionality will your app include?
  - User login and sign up
  - Uploading a user profile picture

Here are a few examples to get you started with. During the proposal stage, you just need to create the tasks. Description and details can be edited at a later time. In addition, more tasks can be added in at a later time.

| Task Name                   | Description                                                                                                   | Example                                                           |
| --------------------------- | ------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| Design Database schema      | Determine the models and database schema required for your project.                                           | (will work on later) |
| Source Your Data            | Determine where your data will come from. You may choose to use an existing API or create your own.           | [Spoonacular](https://spoonacular.com/food-api/docs) |
| User Flows                  | Determine user flow(s) - think about what you want a user’s experience to be like as they navigate your site. | Main page will have search bar for recipe, where user can look up recipes based on ingredients and filters. <br/> Results will include info about the recipe and a link to the recipe. It will be sorted by how many ingredients are missing in increasing order. <br/> For example, if user looks up recipe with tomato, cheese, basil: then top results will include only those 3 and then next results would include those 3 with 1 more ingredient, etc. |
| Set up backend and database | Configure the environmental variables on your framework of choice for development and set up database.        | (will work on later) |
| Set up frontend             | Set up frontend framework of choice and link it to the backend with a simple API call.            | (will work on later) |
| Fix styling.                | Fix styling so that website looks more aesthetic. | (will work on later) |
| User Authentication         | Fullstack feature - ability to authenticate (login and sign up) as a user                                     | Signup will ask for email and password, and maybe default filters (like vegetarian recipes only, no avocados because of allergy, etc.). Logged in users can then save recipes, make meal plans, make grocery lists, etc. <br/> (will work on code later) |

## Labeling

Labeling is a great way to separate out your tasks and to track progress. Here’s an [example](https://github.com/hatchways/sb-capstone-example/issues) of a list of issues that have labels associated.

| Label Type    | Description                                                                                                                                                                                                                                                                                                                     | Example                      |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- |
| Difficulty    | Estimating the difficulty level will be helpful to determine if the project is unique and ready to be showcased as part of your portfolio - having a mix of task difficultlies will be essential.                                                                                                                               | Easy, Medium, Hard           |
| Type          | If a frontend/backend task is large at scale (for example: more than 100 additional lines or changes), it might be a good idea to separate these tasks out into their own individual task. If a feature is smaller at scale (not more than 10 files changed), labeling it as fullstack would be suitable to review all at once. | Frontend, Backend, Fullstack |
| Stretch Goals | You can also label certain tasks as stretch goals - as a nice to have, but not mandatory for completing this project.                                                                                                                                                                                                           | Must Have, Stretch Goal      |

| Task Name                        | Label           | Rationale
| -------------------------------- | --------------- | ------------------
| Design database schema           | Difficult       | Doesn't require coding, but may need to be changed as I code. Need to figure out relationships between data and how to organize it
| Source Your Data                 | Medium          | APIs are already available and API routes are listed out on the docs, but may need to troubleshoot data formats, issues with API calls, etc.
| User flows                       | Difficult       | Need to figure out how to make website user-friendly (setting up routes correctly, making sure users can't access unauthorized routes, making sure filters work, etc.)
| Set up backend/database          | Difficult       | Will use PostgreSQL for database. More familiar with this because of previous assignments. But will probably involve some troubleshooting (need to make sure data is being uploaded properly, and relationships are being set up properly, etc.)
| Set up frontend API call         | Medium          | Will be using axios to make API calls. May need to troubleshoot coding issues 
| Fix styling of website           | Medium          | Not too technical and requires creativity, will need to figure out how to make website user-friendly and aesthetic
| User authentication              | Medium          | Will use bcrypt and other Flask tools for this. More familiar with this because of previous assignments
| Testing                          | Difficult       | Will need to write many unit and integration tests to make sure everything works
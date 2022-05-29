<h2 align="center">reVENUE</h2>
<h4 align="center">A music venue review web app built with Django framework</h4>
<p align="center">Justice Through Code, Columbia University</p>
<p align="center">Jonathan Kirk, Chris Storrer, Jonathan Then</p>

## About

For our final assignment, the WOW Project, we created a Web App in which users can rate various music venues: reVENUE. Our app employs the Minimum Viable Product (MVP) functionality to perform essential functions in the simplest solution for our user(s) to interact with. The user can visit our website to search for reviews of music venues, which are scored based on Food/Drinks, Seating, Cleanliness, Acoustics, Scene/Vibe, and Overall Score. They can leave written comments to accompany their review. The user can post their reviews of the venues already listed, as well as create a new venue on the site to review. Our app employs CRUD functionality. The user can create new reviews which will be inserted into our database; they can read those entries (reviews); they can update their reviewed entries with new or revised information; as well delete reviews completely.  We had a lot of fun creating this project and hope you enjoy it. Rock on!

### Usage

First, please clone a copy of the project into your local directory:

```bash
$ git clone https://github.com/Jonathanlouiskirk/reVENUE.git
```

Then, create a Python virtual environment and activate it in your local project:
(The below activate command is for Mac users; for PC you will need to run django-env\Scripts\activate.ps1).

```bash
$ py -m venv venv
$ . venv/bin/activate
```

Move into the "revenue" directory, and install the packages from `requirements.txt`:

```bash
$ pip install -r requirements.txt
```

To be able to utilize the app with some venues already in it, we created a fixture (a collection of data, within a JSON file).  Please run the following command to load this data:

```bash
$ python manage.py migrate
$ py manage.py loaddata review_data.json
```

Now you are ready to run the server:

```bash
$ py manage.py runserver
```

You are all set!  Visit our app at the following link on your browser: http://localhost:8000/revenue/ 

Tell us what you think!  We'd love your feedback!

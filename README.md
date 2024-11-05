# Xmark #
## A monolithic django project that contains 'Xmarks', a simple bookmark app ##

### Features ###
* Bookmarking
* Tagging
* Categorizing

### Running Locally ###
* Clone the repo
* Create a virtualenv
* Install requirements 
  * `pip install -r requirements/base.txt` for just the app to work
  * `pip install -r requirements/local.txt` for development
* Create a local sqlite db if necessary
* Make a copy of `sample.env` and rename it to `.env` and fill in the values
* Run the server (from the root of the repo)
  * `python manage.py runserver`


### Running Tests ###
* Run `python manage.py test` from the root of the repo
* Run `coverage run manage.py test` to get coverage report
* Run `coverage report` to get coverage report in terminal
* Run `coverage html` to get coverage report in html format

You can also run all the test by using `pytest` from the root of the repo

### Development Notes ###
* Developed by/with/for the Twitch community of [Hannylicious](https://twitch.tv/hannylicious)
* The project is configured to use `django-environ` to load environment variables from `.env` file

### TODO ###
- Logout functionality / redirect to login page
- Add screenshots to the favorites/frequents on load
- Search functionality for bookmarks
- Tagging functionality for bookmarks
- Django Ninja for API for search results?
- Add a middleware for the menu items to be grabbed from JSON stored somewhere in the app and inject into context and rendered 
- Add a favicon
- Add a logo
- Add a footer
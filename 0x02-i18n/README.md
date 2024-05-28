# 0x02. i18n

## Table of Contents
- [Project Overview](#project-overview)
- [Resources](#resources)
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Tasks](#tasks)
  - [Task 0: Basic Flask app](#task-0-basic-flask-app)
  - [Task 1: Basic Babel setup](#task-1-basic-babel-setup)
  - [Task 2: Get locale from request](#task-2-get-locale-from-request)
  - [Task 3: Parametrize templates](#task-3-parametrize-templates)
  - [Task 4: Force locale with URL parameter](#task-4-force-locale-with-url-parameter)
  - [Task 5: Mock logging in](#task-5-mock-logging-in)
  - [Task 6: Use user locale](#task-6-use-user-locale)
  - [Task 7: Infer appropriate time zone](#task-7-infer-appropriate-time-zone)
  - [Task 8: Display the current time](#task-8-display-the-current-time)

## Project Overview
In this project, we will create a Flask application that supports internationalization (i18n) and localization (l10n). The goal is to make the application adaptable to different languages and regions without requiring changes to the codebase.

## Resources
- [Flask-Babel](https://pythonhosted.org/Flask-Babel/)
- [Flask i18n tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xiii-i18n-and-l10n)
- [pytz](http://pytz.sourceforge.net/)

## Learning Objectives
- Parametrize Flask templates to display different languages.
- Infer the correct locale based on URL parameters, user settings, or request headers.
- Localize timestamps.

## Requirements
- All files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3 (version 3.7).
- All files should end with a new line.
- A `README.md` file at the root of the folder of the project is mandatory.
- Code should follow the pycodestyle style (version 2.5).
- The first line of all files should be `#!/usr/bin/env python3`.
- All `.py` files should be executable.
- All modules should have documentation.
- All classes should have documentation.
- All functions and methods should have documentation.
- Documentation should explain the purpose of the module, class, or method.
- All functions and coroutines must be type-annotated.

## Tasks

### Task 0: Basic Flask app
- Setup a basic Flask app with a single route `/`.
- Create an `index.html` template that outputs "Welcome to Holberton" as the page title and "Hello world" as the header.

### Task 1: Basic Babel setup
- Install the Babel Flask extension.
- Instantiate the Babel object and store it in a module-level variable named `babel`.
- Create a `Config` class with a `LANGUAGES` attribute set to `["en", "fr"]`.
- Configure Babel’s default locale and timezone.
- Use the `Config` class as the configuration for the Flask app.

### Task 2: Get locale from request
- Create a `get_locale` function with the `babel.localeselector` decorator.
- Use `request.accept_languages` to determine the best match with the supported languages.

### Task 3: Parametrize templates
- Use the `_` or `gettext` function to parametrize your templates.
- Create a `babel.cfg` file and initialize translations.
- Edit the translation files to provide the correct values for message IDs.
- Compile the dictionaries and ensure the correct messages are displayed.

### Task 4: Force locale with URL parameter
- Implement a way to force a particular locale using the `locale` URL parameter.
- Modify the `get_locale` function to detect the locale parameter and return the appropriate locale.

### Task 5: Mock logging in
- Mock a user login system with a user table.
- Define a `get_user` function to return a user dictionary or None.
- Define a `before_request` function to set the user as a global variable.
- Display a welcome message if a user is logged in, otherwise display a default message.

### Task 6: Use user locale
- Modify the `get_locale` function to use a user’s preferred locale if it is supported.
- Prioritize locale sources as follows: URL parameters, user settings, request header, default locale.

### Task 7: Infer appropriate time zone
- Define a `get_timezone` function with the `babel.timezoneselector` decorator.
- Validate the time zone and use it in the following order: URL parameter, user settings, default to UTC.

### Task 8: Display the current time
- Display the current time on the home page based on the inferred time zone.
- Use the appropriate translations for displaying the time.

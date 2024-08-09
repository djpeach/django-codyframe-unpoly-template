# django-codyframe-unpoly-template
A Django project template with some common django utility packages, unpoly for SPA-like dynamics, and codyframe UI library.

# Setup
Below is a brief explanation of how this project was constructed and reasoning for the choices made.

## Virtual Env
Created with native python `venv` module. 

```shell
python -m venv .venv
source .venv/bin/activate
```

> Optional: Setup Pycharm to manage and use the same python interpreter.

## .gitignore
To allow for other forms of `.env` environment variable files, add `.env.*` and `*.env`. We also don't commit `staticfiles/` and `mediafiles`, as they are generated using django.

## Install and setup Django
Run from root of project and create core module as `_django/` subdirectory, to keep it organized at top of project and clear what its purpose is.

```shell
pip install django
pip freeze > requirements.txt
django-admin startproject _django .
```

## Black
Use [black formatter](https://black.readthedocs.io/en/stable/) to keep python code style consistent.

```shell
pip install black
pip freeze > requirements.txt
black .
```

> Optional: Setup Pycharm file watcher to format `.py` files on changes.

## Database
The `compose.yaml` file contains instructions for running a local postgres instance for this project. Change the database or configuration values as needed. For those that chose to also use postgres and are on certain development machines (ARM Arch, ie M1 Macs), you will also need to install the `psycopg2-binary` as well for this to run locally.

```shell
pip install psycopg2-binary
pip freeze > requirements.txt
```

## Settings & environment variables
Install [django-environ](https://django-environ.readthedocs.io/en/latest/) to read and use environment variables. Create a `.local.env` file for local development environment variables. You can use `.stage.env` and `.production.env` files later on for their respective environments and deployments.

```shell
pip install django-environ
pip freeze > requirements.txt
```

`.local.env`
```text
ENVIRONMENT=LOCAL
DJANGO_SETTINGS_MODULE=_django.settings

SECRET_KEY=localsecretkey

POSTGRES_DB=myproject
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
SQL_HOST=localhost
SQL_PORT=5432
```

Use the environment variables and any others in the django settings file. Depending on how you run your other environments, you may want to create `production.settings.py` and so forth for the correct environments. If you follow this approach, be sure to update the DJANGO_SETTINGS_MODULE accordingly.

View the `_django/settings.py` file to view how these environment variables are used.

## Create `apps/` subdirectory
Using a subdirectory for django apps will keep the root of the file cleaner and separate the configs & assets from the project logic. Note this project does not use `django-admin startapp` or `python manage.py startapp`, as this creates unnecessary boilerplate in many instances. We instead create the requisite files manually when needed. When following this approach, be sure to create a `migrations` module for any app with database models, and an `apps.py` file to define every app. In some apps, it may be desirable to even break down files such as models into appropriate sub-files for organization.

## Templates and static files
Rather than nest static assets and templates away in the django apps, they are housed at the top level of the application. This is due to the designed tight coupling of components as one website, and for ease of access during development. The necessary settings configurations for this have been made.

## Create custom user model
Django recommends at the beginning of every greenfield project to create a custom user. Even if there is no custom functionality currently needed, this provides a base to build from later, as it is difficult to switch to a custom user model later down the road. In the `apps/accounts` app, this project creates a custom user which overrides `AbstractBaseUser`, and removes the requirement for an email during superuser creation. From there it defines some examples of custom user subclasses (Staff and Customer). This could be various levels of staff, admin, and other internal users, or various types of customers, students, tenants, or whatever core user your project's intended audience is. Note how the user model is overridden, subclassed, and used and exposed to the django project in settings, admin, etc.

## Website app
This app will house all the basic website pages and is necessary in essentially every django project. Think of the home page, about-us, FAQ, etc.

## Make File
There is a Makefile with some shorthand utilities for running and managing the server and database. You could also write scripts for this for more complex management utilities.

# Chosen Libraries
This project comes with some chosen libraries that can be helpful in many dango projects. You may choose to keep, remove, or add to these as you see fit.

## django-extensions
For running remediation or other one-off or utility scripts, use the django-extensions script runner functionality. An example of this can be found in the `scripts/` subdirectory, which is where other scripts should also live.

## django-audit-log
This library aids in automating auditing of database model changes. This allows for easily tracking history of an object.

## django-hijack
This library allows authorized users to login as, and impersonate other users. This can be useful for debugging, and for acting on behalf of customers by the staff.

## unpoly
Better for django than htmx due to the lack of need for specific templates and logic to render components. 

## codyframe
You can easily replace this with bootstrap, tailwind, bulma, or whatever you like. This is a premium theme library I have been enjoying.
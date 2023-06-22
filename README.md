<div style="text-align: center">
   <img width=75px height=75px src="static/website/img/favicon.ico" alt="Project logo">
</div>

# <center> Personal Portfolio Website </center>
 <div style="text-align: center">
	Web development using Django and JavaScript and containerized deployment
    <br />
	<!-- Add your project live demo link here -->
    <a href="#>View Demo</a>
    ·
	<!-- Add you issue link here -->
    <a href="https://github.com/jkariukidev/personal-website/issues">Report Bug</a>
    ·
	<!-- Add you issue/discussion link here too -->
    <a href="https://github.com/jkariukidev/personal-website/labels/enhancement">Request Feature</a>
  </div>

<div style="text-align: center">

   [![Status](https://img.shields.io/badge/Personal_Website-Live-success?style=flat-square)](https://jkariukidev.herokuapp.com/)
   ![Status](https://img.shields.io/badge/status-active-success.svg?style=flat-square)
   [![GitHub issues](https://img.shields.io/github/issues/jkariukidev/personal-website?style=flat-square)](https://github.com/jkariukidev/personal-website/issues)
   [![GitHub forks](https://img.shields.io/github/forks/jkariukidev/personal-website?style=flat-square)](https://github.com/jkariukidev/personal-website/forks)
   [![GitHub stars](https://img.shields.io/github/stars/jkariukidev/personal-website?style=flat-square)](https://github.com/jkariukidev/personal-website/stargazers)
   [![GitHub pull requests](https://img.shields.io/github/issues-pr/jkariukidev/personal-website?style=flat-square)](https://github.com/jkariukidev/personal-website/pulls)
   [![GitHub license](https://img.shields.io/github/license/jkariukidev/personal-website?style=flat-square)](https://github.com/jkariukidev/personal-website/blob/main/LICENSE)

</div>
<hr />
<br />
<div style="text-align: center">

   ![me](https://user-images.githubusercontent.com/23359514/227893689-e846c0dc-403a-42ac-a462-4c9d566686f7.jpeg)



</div>
<hr />

## Table of Contents
  - [Description](#description)
  - [Features](#features)
  - [Software](#software)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Tests](#tests)
  - [Deployment](#deployment)
  - [Licenses](#license)
  - [Contributing](#contributing)
  - [Authors](#authors)
  - [Resources](#resources)
  - [Acknowledgement](#acknowledgement)

## Description
This is a simple website that demonstrates full-stack web development using Django and Vanilla JavaScript, CSS and HTML and one that can be forked to your preference.

## Features

Features present in this project include:

1. Responsive and mobile-friendly user interface.
2. User profile management.
3. Static files and user upload management.
4. Local and development deployment.
5. Unit testing.

## ⛏️Software

### Software and Tools

Software used in the development of this project include:
  - **[Python](https://www.python.org/downloads/release/python-3810/)** - Core programming language used in the development of this project. Specific version is referenced in the [development](Dockerfile-dev) and [production](Dockerfile) build configurations.
  - **[Django](https://docs.djangoproject.com/en/4.0/topics/install/)** - Python web development framework that is the main framework used in this project.
  - **[Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)** - Used for version control in development of this project.
  - **[Docker Desktop Windows](https://docs.docker.com/desktop/windows/install/)** - Software for handling development operations (DevOps) using graphical user interface (GUI) in Windows. Installs Docker Command Line Interface, Docker Compose etc.
  - **[Docker Desktop Linux](https://docs.docker.com/desktop/linux/install/)** - Software for handling development operations (DevOps) using graphical user interface (GUI) in Linux.
  - **[Postgres](https://hub.docker.com/_/postgres?tab=tags)** - Object Relational Database Management System used to store and support DB operations in this project. Specific version is referenced in [development](docker-compose-dev.yml) and [production](docker-compose-dev.yml) configurations.

### Dependencies

This project's initial dependencies are listed in the [Pipfile](Pipfile) include: 
* [__Django__](https://docs.djangoproject.com/) as the base framework
* [__django-environ__](https://django-environ.readthedocs.org/) for management of environment variables
* [__psycopg-binary__](https://www.psycopg.org/docs/) database adapter to facilitate database connectivity and other operations.
* [__crispy-bootstrap5__](https://github.com/django-crispy-forms/crispy-bootstrap5) Bootstrap5 template pack for django-crispy-forms.
* [__django-allauth__](https://django-allauth.readthedocs.io/en/latest/) reusable Django app that allows for both local and social authentication
* [__whitenoise__](https://github.com/evansd/whitenoise) for managing static and user uploads in developement and production
* [__pillow__](https://python-pillow.org/) for supporting image processing and capabilities. 
* [__gunicorn__](https://gunicorn.org/) HTTP server for supporting serving of this project over the web
* [__dj-database-url__](https://github.com/jazzband/dj-database-url) support for database URL environment variable
* [__boto3__](https://github.com/boto/boto3) supporting Amazon's S3 capabilities
* [__django-storages__](https://github.com/jschneier/django-storages) support for Amazon's S3 storage backend. Can be used with other storage backends e.g. Digital Ocean, DropBox, Google Cloud etc. 
* [__django-cloudinary-storage__](https://github.com/klis87/django-cloudinary-storage) Package that facilitates integration with Cloudinary using [Django File Storage API](https://docs.djangoproject.com/en/4.1/ref/files/storage/)on management of media and static files.
* [__django-summernote__](http://github.com/summernote/django-summernote) Facilitates integration of [Summernote editor](https://github.com/summernote/summernote) with Django back-end and aids in blog posts creation and editing.
* [__djangorestframework__](https://www.django-rest-framework.org) for provision of WebAPI and REST capabilities.
* [__django-cors-headers__](https://github.com/adamchainz/django-cors-headers) Applied in handling the server headers required for Cross-Origin Resource Sharing (CORS).
* [__djangorestframework-simplejwt__](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/) Provides a JSON Web Token authentication backend for the Django REST Framework.
* [__black__](https://github.com/psf/black) for linting and automatically formatting the code during development
* [__pytest__](https://docs.pytest.org/en/latest/) for writing tests
* [__Django Debug Toolbar__](https://django-debug-toolbar.readthedocs.io/) to help with debugging during development
* [__Faker__](https://faker.readthedocs.io) for generating fake data for use/test in this project (TODO)
* [__coverage__](https://coverage.readthedocs.io/) for measuring code coverage
* [__pytest-django__](https://pytest-django.readthedocs.io/) for testing django specific functionalities during development (TODO)


### Installation
The minimum requirements required to deploy this project is [Docker Engine](). Docker Engine contains docker, [docker compose]() and if on a Desktop environment and prefer a graphical user interface, once can make use of [Docker Desktop]().

[Make](https://www.gnu.org/software/make/manual/make.html) is used in this project to execute docker commands present in the [Makefile](Makefile) for the purpose of saving time that is used during executing long docker commands. This is optional but __recommended__ and can be installed using the following guides
- [Installation on Linux](https://linuxhandbook.com/using-make/)
- Installing make on Windows requires a bit of setup since make is not natively available on the platform. Here are the steps to follow:

   -  Download and install the [Windows Subsystem for Linux](https://learn.microsoft.com/en-us/windows/wsl/install) (WSL) from the Microsoft Store. This will allow you to run a Linux environment on your Windows machine.

    - Once WSL is installed, open the Microsoft Store and search for a Linux distribution that includes make, such as [Ubuntu](https://apps.microsoft.com/store/detail/ubuntu-on-windows/9NBLGGH4MSV6). Download and install the distribution.

    - Open the Linux distribution from the Start menu or by typing the name of the distribution in the search bar.

    - In the Linux terminal, type sudo apt-get update to update the package list.

    - Next, type `sudo apt-get install build-essential` to install the necessary tools for building software, including make.

    - Once the installation is complete, you should be able to use make in the Linux terminal.

Note that you will need to be familiar with using a __Linux command-line interface__ to use make on Windows.

#### Installation on Local / Development 
These are steps that one should take towards deploying this project successfully in a local or development environment which could be in a local machine or similar. 

1. Clone the repository to your local machine.
   ```shell
   git clone  https://github.com/jkariukidev/personal-website.git
   ```
2. Rename the [.env_dev.sample](.env_local.sample) file to `.env` to be used by docker.
3. Add the values for the environment variables. One of the reasons for environment variables is to avoid hard coding passwords and sensitive information on the code. The environment variables include:
   * ``COMPOSE_PROJECT_NAME`` - The project environment state.
   * ``ENVIRONMENT`` - The project environment state. This has been set to `development` for your local machine.
   * ``SECRET_KEY`` - Django cryptography key described in detail [here](https://docs.djangoproject.com/en/4.0/ref/settings/#secret-key).
   * ``DEBUG`` - Variable used in local/development to enable debugging (hence set to ``True`` in development). Read more details [here](https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/#debug).
   * ``ALLOWED_HOSTS`` - List of host/domain names that this Django site can serve. Has been set to `localhost`.
   * ``ENGINE`` - Database backend to use. This project uses PostgreSQL backend by default but can be changed in the environment variables.
   * ``POSTGRES_USER`` - Specifies a user with superuser privileges and a database with the same name. Postgres uses the default user when this is empty.
   * ``POSTGRES_PASSWORD`` - Postgres requires a password to function properly, which is the purpose of this mandatory variable.
   * ``POSTGRES_PORT`` - Network port used by the database also defined in the docker-compose files.
   * ``APP_DB_USER`` - Specifies a database user to be used in this project separate from the database superuser above. This user has been referenced in the [project settings](PersonalWebsite/settings.py) file.
   * ``APP_DB_PASSWORD`` - App user's database password.
   * ``APP_DB_NAME`` - Refers to the database name of this project's database.
   * ``EMAIL_BACKEND`` - The backend to use for sending emails set to `console` in development. Details are well illustrated [here](https://docs.djangoproject.com/en/4.1/topics/email/).
   * ``DEFAULT_FROM_EMAIL`` - The default email to use from this site's manager. Not mandatory in development but can be used for testing purposes.
   * ``EMAIL_HOST`` - Dependent on whether `EMAIL_BACKEND` has been set to anything else besides `django.core.mail.backends.console.EmailBackend`. This is the host to use for sending email.
   * ``EMAIL_HOST_PASSWORD`` - The password for the user for sending service / SMTP defined in the ``EMAIL_HOST``.
   * ``EMAIL_HOST_USER`` - The username for the sending service / SMTP defined in the ``EMAIL_HOST``.
   * ``EMAIL_PORT`` - The port to use for the email sending service.
   * ``EMAIL_USE_TLS`` - This tells the project whether to use secure protocol (port 587) when communicating with email sending service.
   * ``EMAIL_RECIPIENT`` - List of email recipients who will receive emails sent.
4. Build the required docker images for this project using the command.
   ```shell
   make build-dev
   ```
5. Run the development server on http://127.0.0.1:80  by running.
   ```shell
   make runserver-dev
   ```
6.  Apply migrations to synchronize the database state with the current set of models and migration using.
   ```shell
   make migrate-dev
   ```
   in the event [website's models](website/models.py) or [accounts' models](useraccounts/models.py) are altered, one can update migrations which generates the SQL commands for preinstalled apps by running
   ```shell
   make makemigrations-dev
   ```
7. __Optional__: Load initial data making use of [django fixtures](https://docs.djangoproject.com/en/4.1/howto/initial-data/). 
   * User accounts - This creates a default superuser (testadmin) and a standard user (testuser). The superuser can log into the Django admin panel and change settings etc.
      ```shell
      make load-user-data
      ```
   * Blog posts and portfolio projects - This populated the database with sample blog posts, post categories, post comments and portfolio projects. One is at liberty to add their own. NOTE that this should be only run after creating user accounts above. 
      ```shell
      make load-website-data
      ```
8. If skipped the previous step, create your own additional superuser by running.
   ```shell
   make superuser-dev
   ```
9. If populated the database using step 7 above, one can try logging in using the following:
   * Navigate to the admin login URL at http://127.0.0.1:8000/mkubwa/
   * Log in using `testadmin` as user and `UserAdmin123` as password. (NOTE: this is the superuser with full privileges on this app)
   * Or navigate to the user login URL at http://127.0.0.1:8000/useraccounts/login/
   * Log in using `testuser@email.com` as user email and `UsualUser123` as password. (NOTE: this user cannot log into admin panel)
10. Logs can be monitored by running.
    * `make logs-dev` - Prints log output
    * `make logs-interactive-dev` - Show logs interactively
11. On shutting down the development server, run the following.
    * `make shutdown-dev` which stops the running containers (web and database)
    * `make shutdown-volumes-dev` which stops the running containers and deletes volumes which contain persisted data.

#### Installation on Production
These are steps that one should take towards deploying this project successfully in a production environment which could be in a cloud virtual machine (VM) making the project accessible through the internet.

1. Clone this project using `git clone ` command.
      ```shell
     git clone https://github.com/jkariukidev/my-demo-website.git
     ```
  2. Navigate into the cloned project folder and using a terminal/shell or otherwise, rename the [env_prod.sample](.env_prod.sample) to `.env` in production to be recognized by docker.
  3. Edit the environment variables as required and ensure you do not share passwords and secure keys with the public. The additional environment variables for production include:
     * ``ENVIRONMENT`` - The project environment state. Set this to `production` in your in public server host.
     * ``DEBUG`` - Must be set to `False` to avoid leaking sensitive project and server information displayed during development.
     * ``ALLOWED_HOSTS`` - List of host/domain names that this Django site can serve. Has been set to your domain otherwise the website may not be accessed.
     * ``EMAIL_BACKEND`` - This is the backend to use for email. Django supports various  [email backends](https://docs.djangoproject.com/en/4.1/topics/email/#topic-email-backends).
     * ``DEFAULT_FROM_EMAIL`` - The default email to use from this site's manager. 
     * ``EMAIL_HOST`` - This is the host to use for sending email.
     * ``EMAIL_HOST_USER`` - The username for the sending service / SMTP defined in the ``EMAIL_HOST``
     * ``EMAIL_HOST_PASSWORD`` - The password for the user for sending service / SMTP defined in the ``EMAIL_HOST``
     * ``EMAIL_PORT`` - The port to use for the email sending service.
     * ``EMAIL_USE_TLS`` - This tells the project whether to use secure protocol (port 587) when communicating with email sending service.
     * ``CLOUDINARY_CLOUD_NAME`` - Mandatory variable pointing to the name of the cloud provided by [cloudinary](https:://cloudinary.com)
     * ``CLOUDINARY_API_KEY`` - Mandatory API key associated with a given cloudinary account.
     * ``CLOUDINARY_API_SECRET`` - Secret key associated with the `CLOUDINARY_API_KEY`
     * ``CLOUDINARY_URL`` - Combination of the `CLOUDINARY_API_KEY`, `CLOUDINARY_API_SECRET` and `CLOUDINARY_CLOUD_NAME` which constitutes of the Cloudinary URL.
     * ``MEDIA_URL`` - URL that handles the media files served
     * ``DEFAULT_FILE_STORAGE`` - Default file storage class to be used for any file-related operations
     * ``STATIC_URL`` - URL to use when referring to static files located
     * ``STATICFILES_STORAGE`` - The file storage engine to use when collecting static files with the collectstatic management command.
     
  4. Run the docker services for this project using compose in production environment.
     ```
     make runserver
     ```
  5. Propagate models into your database schema using the [migrate command](https://docs.djangoproject.com/en/4.0/ref/django-admin/#migrate). Note
     that this command is being run inside the docker web container. Refer for more on [exec docker command](https://docs.docker.com/engine/reference/commandline/compose_exec/).
     ```
     make migrate
     ```
  6. Check logs using `make logs` or to view the logs interactively use `make logs-interactive`

For several other commands, view them in the [Makefile](Makefile)

## Usage

  - Customizing and deploying personal website.
  - Blogging and blog posts management
  - User account and profile management
  - Email SMTP service 
  - Email authentication
  - REST API - Token authentication, managing blog posts via GET, POST and PUT.
  - Static files assets management using services; Cloudinary, AWS S3 etc.

## Tests
TBD

## Deployment
TBD

## 💳License

<!-- Mention your project licence here and also link to that file -->

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

## Contributing
  If you want to contribute to a project and make it better, your help is welcome. Contributing is also a great 
  way to learn more about social coding on GitHub, new technologies and their ecosystems and how to make constructive, 
  helpful bug reports, feature requests and the noblest of all contributions: a good, clean pull request.


## ✍️Authors

- [@Joseph Kariuki](https://www.github.com/jkariukidev) - Idea & Initial Work

## 🧬Resources

List all the articles, videos or docs you referred while building this project for eg:

<!-- Add links to all the resources you followed or referred to -->

- [Django Docs](https://docs.djangoproject.com/en/4.1/)
- [Learn Django](https://learndjango.com/)
- [GetBootstrap](https://getbootstrap.com)
- [JQuery](https://jquery.com/)
- [Docker Documentation](https://docs.docker.com/)
- [ChatGPT](https://chat.openai.com)

## 🎉Acknowledgement

- [William Vincent](https://github.com/wsvincent) 
- [John Elder](https://github.com/flatplanet)

<div style="text-align: center">
   <img width=75px height=75px src="static/website/img/favicon.ico" alt="Project logo">
</div>

<h1>Personal Portfolio Website</h1>
 <p style="text-align: center">
 	<!-- Add your tagline or very short intro of your project -->
    A personal portfolio website and blog project.
    <br />
	Demonstration of web development using Django
    <br />
	<!-- Add your project live demo link here -->
    <a href="https://jkariukidev.herokuapp.com">View Demo</a>
    ·
	<!-- Add you issue link here -->
    <a href="https://github.com/jkariukidev/personal-website/issues">Report Bug</a>
    ·
	<!-- Add you issue/discussion link here too -->
    <a href="https://github.com/jkariukidev/personal-website/labels/enhancement">Request Feature</a>
  </p>

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

   ![image](https://user-images.githubusercontent.com/23359514/184578198-b766699f-636c-4ed8-bad8-649231882848.png)


</div>
<hr />
<p style="text-align: center">
   Personal portfolio website is a simple and interactive website and blog that has been developed using Django and Bootstrap. It took me a few weeks to 'complete' and deploy it.
</p>

## About

Personal portfolio website is aimed at demonstrating the capabilities of Django, a Python web framework which has been 
used for the backend and Bootstrap which has been used to design the front-end and JQuery.

## Features

Features and functionalities demonstrated in this project:

1. Responsive pages and controls (forms, buttons, navigation etc.)
2. User account management - Login, Logout, registration etc.
3. Management of static files (Images, JS and Cascading Style Sheets)
4. HTML styling of blog posts and attaching media content.

## ⛏️Built with

- Python & Django
- Bootstrap & JQuery
- PostgreSQL
- Docker & Docker Compose

## Getting Started

This project requires Python (version 3.10 or higher), Git, and Docker. See [deployment](#Deployment) for 
notes on how to deploy the project on production.

### Prerequisites

- Python 3.10
- PostgreSQL
-  For production, PaaS supporting Web Server Gateway Interface (WSGI) and container deployments e.g. Heroku, DigitalOcean etc.

### Installation

#### Local or Development environment

Step by step methods to guide the reader how to set up local dev environment:

1. Clone this repo `git clone https://github.com/jkariukidev/personal-website.git`
2. Copy the provided [environment variable file](.env_dev.sample) and be sure to refer to [Docker practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/) with respect to
variable name and value assignment. 
   ```shell
   mv .env_dev.sample .env_dev
   ```
3. Update the [Django's cryptographic key](https://docs.djangoproject.com/en/4.1/topics/signing/) named SECRET_KEY. Three ways in generating this key include:
   * Drop into a Python shell and leverage on [Python secrets](https://docs.python.org/3/library/secrets.html) module.
   ```shell
   import secrets
   
   print(secrets.token_urlsafe())
   ```
   OR
   ```shell
   import secrets 
   
   length = 50
   chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
   secret_key = ''.join(secrets.choice(chars) for i in range(length))
   print(secret_key)
   ```
   * If in Python Django environment (virtualenv), drop into the Django shell and run the following.
   ```shell
   from django.core.management.utils import get_random_secret_key
   
   print(get_random_secret_key())
   ```
4. The other variables include:
   * ENVIRONMENT - Specifies the environment which you are working on. The two recommendations are `development` and `production`
   * DEBUG - Django's debug feature enabling you to see display of error pages. In development, one can keep this set to `True`. Detailed reference [here](https://docs.djangoproject.com/en/4.1/ref/settings/#debug).
   * POSTGRES_DB - Optional variable that sets the PostgreSQL's default Database name. [Details here](https://github.com/docker-library/docs/blob/master/postgres/README.md#postgres_db).
   * POSTGRES_USER - Optional variable that is used together with POSTGRES_PASSWORD and sets the PostgreSQL's default Database user. [Details here](https://github.com/docker-library/docs/blob/master/postgres/README.md#postgres_user).
   * POSTGRES_PASSWORD - Optional variable that sets the PostgreSQL's default Database name. [Details here](https://github.com/docker-library/docs/blob/master/postgres/README.md#postgres_password).
   * POSTGRES_PORT - PostgreSQL database networking port well known as the TCP port. By default, it runs on port 5432 but can be altered. [Details here](https://www.postgresql.org/docs/14/runtime-config-connection.html).
   * POSTGRES_HOST - Variable corresponding to the IP address or host name through which database server is running on. In this case, it is same as [database service in compose file](docker-compose-dev.yml).
5. Pull and build images using docker compose. Note that if you are running in development use [docker-compose-dev.yml](docker-compose-dev.yml).
   ```shell
   docker compose -f docker-compose-dev.yml up -d
   ```
   the `up` command starts up the container while the `-d` instructs docker to run the containers in a [detached](https://docs.docker.com/engine/reference/run/#detached-vs-foreground) mode. 
6. Apply the current migrations in [migrations directory](website/migrations/) to the database via the command.
   ```shell
   docker compose -f docker-compose-dev.yml exec web python manage.py migrate
   ```
7. Create a superuser to access the Django admin site. 
   ```shell
   docker compose -f docker-compose-dev.yml exec web python manage.py createsuperuser
   ```
8. Navigate to http://localhost:8000 in your favorite browser. The homepage will load and appears as shown below.

![image](https://user-images.githubusercontent.com/23359514/164234454-cfdaab7c-2135-4cdb-8c22-58495efb7bf0.png)

#### Production environment
TBD

##### Docker
TBD
##### Heroku
Below are summarized steps in deploying the project to [Heroku](https://www.heroku.com/). The project has already been
configured for deployment on heroku.
1. Create an account on Heroku. [Here is the guide](https://signup.heroku.com/).
2. Download and install [Heroku Command Line Interface](https://devcenter.heroku.com/articles/heroku-cli#install-the-heroku-cli) (CLI). 
3. Navigate in the project directory and ensure python virtual environment is active and log into Heroku using the CLI 
with the command below. It should ask you for your login credentials.
   ```shell
    heroku login
   ```
4. Create a new app on Heroku via the CLI. You can optionally name your app using a unique name that hasn't been used on Heroku. If left empty
heroku will assign it a name. For more on app creation refer [here](https://devcenter.heroku.com/articles/creating-apps).
   ```shell
    heroku create
   ```
5. Disable the collection of static files by heroku by setting the below variable. We may not want Heroku running collectstatic for you. Details 
[here](https://devcenter.heroku.com/articles/django-assets#disabling-collectstatic).
   ```shell
    heroku config:set DEBUG_COLLECTSTATIC=1
   ```
6. Export the SECRET_KEY environment variable. Refer [here](https://devcenter.heroku.com/articles/config-vars#managing-config-vars) for more detail on Heroku system variables. The XXX
represents the Django SECRET_KEY explained in previous steps.
   ```shell
    heroku config:set SECRET_KEY='XXXX'
   ```
7. Export the Django setting variable to point to the production configuration which has been set to be applied in a 
   production environment.
   ```shell
    heroku config:set DJANGO_SETTINGS_MODULE=PersonalWebsite.settings.pro
   ```
8. Push any pending commits to GitHub.
   ```shell
   git add -A 
   git commit -m '<message>'
   git push 
   ```
9. Push the code to heroku.
   ```shell
   git push heroku main
   ```
10. Set Heroku to use the free tier processes for our web app.
    ```shell
    heroku ps:scale web=1
    ```
11. Visit the URL shown in the command line log after deployment process. In my case, it is https://jkariukidev.herokuapp.com

### PythonAnywhere

PythonAnywhere supports deployment of Python applications including Django. For more detail on deploying this or any
other Django project on PythonAnywhere, refer to their [documentation](https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/).

### DigitalOcean

This [Digital Ocean tutorial](https://docs.digitalocean.com/tutorials/app-deploy-django-app/) illustrates on the steps
for deploying Django-based applications on their platform.

## Testing
TBD 

## TBD

List of enhancements to be effected on this project. For more, add recommendation on the issues section and label them as enhancements. 

- Social authentication
- Post tagging functionality
- Full-text search functionality
- Post likes (Redis incorporation)
- CI/CD

## Future Plans

List of future plans with this project.

- Spread the gospel of web development using Django.
- Help interested persons start up with a personal portfolio website.
- A pre-amble to future Django-based projects

## Usage

One can take the advantage of this project to create their own portfolio website with the following illustrations:
- Blog functionality
- Post authoring
- User registration
- Sharing content

## ✍️Authors

<!-- Add links to all the authors profile here OPTIONAL: You can mention what they did as well -->

- [@Joseph Kariuki](https://www.github.com/jkariukidev) - Idea & Initial Work
- [@DeeshanSharma](https://www.github.com/DeeshanSharma) - Markdown documentation

## 📢Contributors

<!-- Add links to all the contributors profile here -->

- [@Joseph Kariuki](https://www.github.com/jkariukidev)

## 💳License

<!-- Mention your project licence here and also link to that file -->

Distributed under the MIT License. See [`LICENSE`](LICENCE) for more information.

## 🧬Resources

List all the articles, videos or docs you referred while building this project for eg:

<!-- Add links to all the resources you followed or referred to -->

- [Django Docs](https://docs.djangoproject.com/en/4.0/)
- [GetBootstrap](https://getbootstrap.com/docs/4.1/getting-started/introduction/)
- [JQuery](https://jquery.com/)
- [Django for Beginners](https://www.amazon.com/Django-Beginners-Learn-web-development/dp/1980377898)

## 🎉Acknowledgement

Acknowledge all whose code you used, or took inspiration from or mention any websites you used in the development for eg:

- [John Elder](https://github.com/flatplanet) 
- [Shields](https://shields.io)
- [Choose License for your Project](https://choosealicense.com)

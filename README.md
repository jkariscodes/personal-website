<div align="center">

<!-- Add your project logo if you have any -->
<img width=75px height=75px src="static/website/img/favicon.ico" alt="Project logo">

</div>

<h1 align="center">Personal Portfolio Website</h1>

 <p align="center">
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

<div align="center">

<!-- Use Shields website (link in acknowledgement section) to generate these for your repo or just replace the links here with yours -->

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

<div align="center">

<!-- Add your project demo gif here -->

![Project Demo Gif](https://jkariukidev.herokuapp.com/static/website/img/interactive_website.797b82f28d73.jpg)

</div>

<!-- You may write notes in your readme this way if you want to, it looks good and also different from other text -->



<hr />

<p align="center">Personal portfolio website is a simple and interactive website and blog that has been developed using 
Django and Bootstrap. It took me a few weeks to 'complete' and deploy it.</p>

## About

Personal portfolio website is aimed at demonstrating the capabilities of Django, a Python web framework which has been 
used for the backend and Bootstrap which has been used to design the front-end and JQuery.

## Features

Features and functionalities demonstrated in this project:

1. Responsive pages and controls (forms, buttons, navigation etc.)
2. New user registration
3. User profile management for registered users
4. User authentication
5. Handling of static files (Images, Scrpts and Cascading Style Sheets)
6. HTML styling of blog posts and attaching media content.

## ⛏️Built with

Modules, frameworks, package, dependencies etc in bullet points. Add-ons/plugins can be found in acknowledgements 
section.

- Python
- Django
- Bootstrap
- JQuery

## Getting Started

This project requires Python (version 3.8 or higher) and Git at the very minimum. See [deployment](#Deployment) for 
notes on how to deploy the project on a live system.

### Prerequisites

- Python 3
- Pipenv / pip
- Django
- Web Server Gateway Interface (WSGI) server e.g Heroku, PythonAnywhere, Heroku etc.
- Git

### Installation

Step by step methods to guide the reader how to setup local dev environment for eg:

1. Clone this repo `git clone https://github.com/jkariukidev/personal-website.git`
2. Install all the dependencies either using pipenv or pip. My preference is pipenv. Read more in
[this pipenv guide](https://docs.pipenv.org/).
   ```commandline
   cd personal-website
   pipenv shell
   pipenv install -r requirements.txt
   ```
3. Important! Generate Django secret key required for your project to run using:
    - [django-secret-key-generator](https://django-secret-key-generator.netlify.app/) and copy it to the clipboard. 
   The key generator appears as shown below.
   ![image](https://user-images.githubusercontent.com/23359514/164235413-dc49b194-35bf-4c8f-b628-26569da94e90.png)
    - [Django cryptographic signing](https://docs.djangoproject.com/en/4.0/topics/signing/). In your terminal/CommandPrompt enter the following:
   ```python
   python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
   ```
   ![image](https://user-images.githubusercontent.com/23359514/164235052-102c5b8e-367d-487e-b1b3-9fafed1e26cc.png)
   - [Python secrets](https://docs.python.org/3/library/secrets.html#module-secrets). An alternative to the two above. 
   This assumes you have Python already installed as it exists in the Python Standard Library. In your CMD/terminal enter:
   ```python
   python3 -c "import secrets; print(secrets.token_urlsafe(50))"
   ```
   ![image](https://user-images.githubusercontent.com/23359514/164235182-a0261f3f-312a-47a1-b5b4-92215bfec343.png)

4. Set the copied secret_key as shown below, where `XXXXXXXXX` represents the key.: <br>
   - Linux: `export SECRET_KEY="XXXXXXXXX"` <br> 
   - Windows Command Prompt (CMD): `set SECRET_KEY="XXXXXXXXX"` <br> 
   - Windows Powershell: `Set-Item -Path Env:\SECRET_KEY -Value "XXXXXXXXX"`
5. Modify the text and images (Front-end) as you wish. Knowledge in HTML, CSS, JavaScript, Bootstrap and Django is required.
6. For development testing locally, assign DJANGO_SETTINGS variable to the local configuration using the following 
   command in your terminal.
   ```shell
   export DJANGO_SETTINGS_MODULE=PersonalWebsite.settings.local
   ```
   OR to use the production configuration,
   ```shell
   export DJANGO_SETTINGS_MODULE=PersonalWebsite.settings.pro
   ```
7. Create/update the database schema (we are using default SQLite database).
   ```python
   python manage.py migrate
   ```
8. Create a superuser to administer this website.
   ```python
   python manage.py createsuperuser
   ```

9. Run the local development server. Note the additional settings variable pointing to the local settings configuration.
   ```python
   python manage.py runserver
   ```
10. Open the website in the URL https://localhost:8000 and it should appear as shown below.
![image](https://user-images.githubusercontent.com/23359514/164234454-cfdaab7c-2135-4cdb-8c22-58495efb7bf0.png)

10. To end the local server, type Ctrl+C on your keyboard. 

## Deployment

This project is productionready with few enhancements to be done. According to 
[Django deployment referecne](https://docs.djangoproject.com/en/4.0/howto/deployment/), this project can be deployed via
the [Web Server Gateway Interface](https://wsgi.readthedocs.io/en/latest/) (WSGI) or [Asynchronous Server Gateway
Interface](https://asgi.readthedocs.io/en/latest/) (ASGI). The WGSI is being employed in this project. 

### Heroku
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

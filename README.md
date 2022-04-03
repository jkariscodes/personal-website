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
Django and Bootstrap. It took me a
few weeks to complete and deploy it.</p>

## About

Personal portfolio website is aimed at demonstrating the capabilities of Django, a Python web framework which has been 
used for the backend and Bootstrap 
which has been used to design the front-end and JQuery.

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
cd personal project
pipenv install -r requirements.txt
```
3. Modify the text and images as you wish. Knowledge in HTML, CSS, JavaScript and some Django template may be required.
4. Create/update the database schema (we are using default SQLite database).

```python
python manage.py migrate
```
5. Create a superuser to administer this website.
```python
python manage.py createsuperuser
```
6. Important! Generate Django secret key required for your project to run using 
[this site](https://django-secret-key-generator.netlify.app/) 
and copy it to the clipboard. The key generator appears as shown below.
7. Set the copied secret_key as shown below, where `XXXXXXXXX` represents the key.: <br>
Linux: `export SECRET_KEY="XXXXXXXXX"` <br> 
Windows Command Prompt (CMD): `set SECRET_KEY="XXXXXXXXX"` <br>
Windows Powershell: `Set-Item -Path Env:\SECRET_KEY -Value "XXXXXXXXX"`

8. Run the local development server. Note the additional settings variable pointing to the local settings configuration 
9. file.
```python
python manage.py runserver --settings=PersonalWebsite.settings.local
```
7. Open the website in the URL _https://localhost:8000_ and it should appear as shown below. 
8. To end the local server, typie Ctrl+C on your keyboard. 

## Deployment

This project is deployment-ready with few enhancements to be done. According to 
[Django deployment referecne](https://docs.djangoproject.com/en/4.0/howto/deployment/), this project can be deployed via
the [Web Server Gateway Interface](https://wsgi.readthedocs.io/en/latest/) (WSGI) or [Asynchronous Server Gateway
Interface](https://asgi.readthedocs.io/en/latest/) (ASGI). The WGSI is being employed in this project. 

### Heroku
TBD

[//]: # (1. To test production configuration, run the following)

[//]: # (2. Push your code to it)

[//]: # (3. Create New Project on your [Vercel Dashboard]&#40;https://vercel.com/dashboard&#41;)

[//]: # (4. Import your Git Repository)

[//]: # (5. After successful import, changes made to the Production Branch &#40;commonly "main/master"&#41; will be a Production Deployment and rest all branches will generate Preview Deployments.)

[//]: # (6. Once deployed, you will get a URL for your live app, such as: `https://xyz.vercel.app`)

### PythonAnywhere
TBD

[//]: # (1. To test production configuration, run the following)

[//]: # (2. Push your code to it)

[//]: # (3. Create New Project on your [Vercel Dashboard]&#40;https://vercel.com/dashboard&#41;)

[//]: # (4. Import your Git Repository)

[//]: # (5. After successful import, changes made to the Production Branch &#40;commonly "main/master"&#41; will be a Production Deployment and rest all branches will generate Preview Deployments.)

[//]: # (6. Once deployed, you will get a URL for your live app, such as: `https://xyz.vercel.app`)

### DigitalOcean

TBD

[//]: # (1. To test production configuration, run the following)

[//]: # (2. Push your code to it)

[//]: # (3. Create New Project on your [Vercel Dashboard]&#40;https://vercel.com/dashboard&#41;)

[//]: # (4. Import your Git Repository)

[//]: # (5. After successful import, changes made to the Production Branch &#40;commonly "main/master"&#41; will be a Production Deployment and rest all branches will generate Preview Deployments.)

[//]: # (6. Once deployed, you will get a URL for your live app, such as: `https://xyz.vercel.app`)

## TBD

List of enhancements to be effected on this project. For more, add recommendation on the issues section and label them as enhancements. 

- Email configuration
- User email and social authentication
- Post tagging functionality
- Full-text search functionality
- Post likes (Redis incorporation)
- Unit tests
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

## 📖Contributing

**_"In real open source, you have the right to control your own destiny."_** _- Linus Torvalds_

## 📢Contributors

It is good to give credit to your contributors as they have given their precious time working on your project so list their name with contact details for eg:

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

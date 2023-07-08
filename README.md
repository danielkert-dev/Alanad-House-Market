##### **The repo** https://github.com/danielkert-dev/Django-auth-template

This is a template to start a basic authentication base with Django, from which you can start projects that need authentication. I'm trying to simplify as much as possible with this because it's for personal use, but anyone can use this. It is intermediate, so it does not go into detail about how to set up the database and install Django. 

-------------

### Django setup

Setup Postgres database (Recommended with pgAdmin) and create a database.
**Tutorial** https://www.geekbits.io/how-to-install-postgresql-and-pgadmin-4-on-windows/

Install Django and all the necessary things by looking at the official site. Start the project and core app:
**Django official** https://docs.djangoproject.com/en/4.2/intro/tutorial01/

```bash
django-admin startproject project
cd project/
python manage.py startapp core
python manage.py runserver #localhost:8000
```

Install the needed packages: 
**django-allauth** https://django-allauth.readthedocs.io/en/latest/

```bash
pip install asgiref Django gunicorn psycopg2 sqlparse whitenoise python-decouple django-allauth crispy crispy-bootstrap5
```

GitHub repository with .gitignore, .env, .requirements.txt (For packages) files:

```gitignore
.env
```

If there is a problem that gitignore doesn't work then clear cash in the project folder

```bash
git rm -r --cached .
```

The environment variables. Create an app password for the Google authentication social account.  
**Google** https://support.google.com/accounts/answer/185833?hl=en

```env
# DATABASE Postgres
PGDATABASE=databasename 
PGHOST=localhost
PGPASSWORD=password
PGPORT=5433
PGUSER=postgres

# GOOGLE EMAIL
EMAIL_HOST_USER=coolguy@gmail.com
EMAIL_HOST_PASSWORD=16randomletters #App password

#MIX
ACCOUNT_DEFAULT_HTTP_PROTOCOL=http #For production purpouse
```

All the requirements for when sending into production

```requirements
asgiref==3.5.2
Django==4.0.4
gunicorn==20.1.0
psycopg2==2.8.6
sqlparse==0.4.2
whitenoise==6.2.0 # For temorary picture files. Bitbucket, AWS S3 or B2 Cloud

python-decouple           # 3.8
django-allauth            # 0.54.0
crispy                    #0.7.4
crispy-bootstrap5         #0.7
```

#### Base setup

In the `project/settings.py` change/add:

```python

# For environment variables and static file dir.
import os
from decouple import config

# Change this after when in production for more security
ALLOWED_HOSTS = ["*"]

# All the allauth apps and the core app. Also the crispy forms to make the form nice later
INSTALLED_APPS = [
	# The boilerplate django.bla.bla

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    
    'crispy_forms',
    'crispy_bootstrap5',
    
    'core',
]

# For withenoise (Image storage that can later be changed)
MIDDLEWARE = [
	# The boilerplate django.bla.bla
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

# So that we can make a templates folder in the base dir
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"], #Change this!
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Change the default database
DATABASES = {

    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('PGDATABASE'),
        'USER': config('PGUSER'),
        'PASSWORD': config('PGPASSWORD'),
        'HOST': config('PGHOST'),
        'PORT': config('PGPORT'),
    }
}

# For static files
STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

#Allauth

# Redirect for when logged in
LOGIN_REDIRECT_URL = 'core:index'
LOGIN_URL = 'account_login'
LOGOUT_URL = 'account_logout'

# Whitch site configuration should be used
SITE_ID = 1


# This loggs in directly after useing the social account (Google login)
SOCIALACCOUNT_LOGIN_ON_GET = True

# Its a blackbox for giving allauth the perms
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

# We are useing Google as the option for logging in. (There are others that can be added)
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': config('GOOGLE_CLIENT_ID'),
            'secret': config('GOOGLE_CLIENT_SECRET'),
            'key': '',
        }
    }
}

# Email configurations
ACCOUNT_EMAIL_VERIFICATION = 'optional'
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS=3
ACCOUNT_CONFIRM_EMAIL_ON_GET= True
ACCOUNT_EMAIL_REQUIRED = True

# CRISPY FORMS

# Crispy template. You can use bootsrap4 instead if needed
CRISPY_TEMPLATE_PACK = 'bootstrap5'

# When pushing to production that hass https you can take out the variable in .env
ACCOUNT_DEFAULT_HTTP_PROTOCOL = config('ACCOUNT_DEFAULT_HTTP_PROTOCOL', default='https')

# EMAIL BACKEND

# All the email details for sending emails
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST= 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
# EMAIL_USE_SSL = False
########################
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
########################

```

Create a file in the core app folder `urls.py` and folders called `templates/core` and in the folder create `index.html`, `base.html`, `header.html`. Add the static folder with css and js (This is extra but can be changed later depending on use). Then download the allauth templates from source code and add to the project (Or download from this project that has ready templates). The file system should look like this.
**Templates** https://github.com/pennersr/django-allauth/tree/main/allauth/templates

```folder
└───project
    │   manage.py
    ├───core
    │   │   admin.py
    │   │   apps.py
    │   │   models.py
    │   │   tests.py
    │   │   urls.py
    │   │   views.py
    │   │   __init__.py
    │   ├───migrations
    │   ├───templates
    │   │   └───core
    │   │           base.html
    │   │           header.html
    │   │           index.html
    │   └───__pycache__
    │
    ├───project
    │   │   asgi.py
    │   │   settings.py
    │   │   urls.py
    │   │   wsgi.py
    │   │   __init__.py
    │   └───__pycache__
    │
    │
    ├───static
    │   ├───css
    │   │       stylesheet.css
    │   └───js
    │           colorMode.js
    │
	└───templates # This should have all the templates.html, more in detail later
        ├───account
        ├───openid
        ├───socialaccount
        └───tests
```


In the `project/core/templates/core/base.html` we set the base of the templates.

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  
    <title>{% block title %}{% endblock %}</title>
  
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@500&display=swap" rel="stylesheet">

    <!--Bootstrap-->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.14.7/dist/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
  
  
    <!-- CSS -->
    <link rel="stylesheet" href="{% static 'css/stylesheet.css' %}">
  
    <!-- JS -->
    <script src="{% static 'js/colorMode.js' %}"></script>
  
  
</head>
<body class="">
    {% include "core/header.html"%}
        {% block content %}
        {% endblock %}
</body>
</html>
```

In the `project/core/templates/core/header.html` we set the header.

```html
<header class="p-2 bg-secondary text-white">
        <div class="d-flex flex-wrap justify-content-center align-items-center w-100">
            <a href="{% url 'core:index' %}" class="h4 col-xl my-auto my-2 title text-white">Title</a>
            
                <!-- Links -->
                <div class="d-flex col-sm-auto justify-content-end align-items-center" style="max-width: fit-content;">

                        <!-- If not logged in, login button-->
                        {% if request.user.is_authenticated %}
                            {% if request.path != '/profile/' %} <!-- Add this line -->
                                <a href="{% url 'account_email' %}" class="btn btn-primary btn-sm mx-1 my-1">{{ request.user.username|truncatechars:14 }}</a>
                            {% endif %}                            

                            <!-- Nav burger-->
                            <a class="btn  btn-primary btn-sm mx-1 my-1" data-toggle="collapse" href="#collapseNav" role="button" aria-expanded="false" aria-controls="collapseNav">
                                &#9776;
                            </a>
                            <a href="{% url 'account_logout' %}" class="small text-muted mx-1" title="Click to logout!">
                                <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-power" width="16" height="16" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
                                    <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
                                    <path d="M7 6a7.75 7.75 0 1 0 10 0" />
                                    <path d="M12 4l0 8" />
                                  </svg>
                            </a>

                        {% else %}
                            <a href="{% url 'account_login' %}" class="btn btn-primary btn-sm mx-2 my-1">Login</a>
                            <a href="{% url 'account_signup' %}" class="btn btn-primary  btn-sm mx-2 my-1">Signup</a>
                        {% endif %}

                        <a onclick="toggleTheme()" class="small text-muted mx-1">
                            <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-sun-high" width="16" height="16" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
                                <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
                                <path d="M14.828 14.828a4 4 0 1 0 -5.656 -5.656a4 4 0 0 0 5.656 5.656z" />
                                <path d="M6.343 17.657l-1.414 1.414" />
                                <path d="M6.343 6.343l-1.414 -1.414" />
                                <path d="M17.657 6.343l1.414 -1.414" />
                                <path d="M17.657 17.657l1.414 1.414" />
                                <path d="M4 12h-2" />
                                <path d="M12 4v-2" />
                                <path d="M20 12h2" />
                                <path d="M12 20v2" />
                              </svg>
                        </a>
                </div>
            </div>

        {% if request.user.is_authenticated %}
        <div class="collapse" id="collapseNav">
            <div class="d-flex col-sm-auto justify-content-center align-items-center">
                <a href="" class="text-white p-2">Home</a>
                <a href="" class="text-white p-2">About</a>
                <a href="" class="text-white p-2">Contact</a>
            </div>
        </div>
        {% endif %}
</header>
```

In the `project/core/templates/core/index.html` we set the index.

```html
{% extends 'core/base.html' %}
{% block title %}Welcome!{% endblock %}
{% block content %}
{% for message in messages %}
    <div class="alert {{ message.tags }} alert-dismissible shadow bg-danger fade show rounded m-2" role="alert">
        <button type="button" class="close small" data-dismiss="alert" aria-label="Close">
            <span aria-hidden="true">&times;</span>
        </button>
        {{ message | safe }}
    </div>

{% endfor %}
{% if request.user.is_authenticated %}
<p>Your username</p>
{{ request.user.username|truncatechars:14 }}
{% endif %}
<p>Text</p>

  

{% endblock %}
```

In the `project/static/css/stylesheet.css` we set all the base styling.

```css
:root {
  --first-color: #1e1e1e;
  --second-color: #262626;
  --third-color: #363636;
  --icon-color: #A4A4A4;
  --text-color: #DADADA;

  --blue-lightest: #D5E9F7;
  --blue-lighter: #AED4F3;
  --blue-light: #87BEEF;
  --blue-medium: #5AA8E9;
  --blue-dark: #3392DD;
  --blue-darker: #1F6EBB;
  --blue-darkest: #115499;
  --blue-deepest: #0A4077;
  --blue-blackest: #052855;
  }
  
/* General */
body {
    font-family: 'Inter', sans-serif !important;
  }
  a {
    text-decoration: none; /* no underline */
  }
  a:hover {
    text-decoration: none;
  }

/* Theme */

/* Dark Theme */
.dark-theme {
  --first-color: #1e1e1e;
  color: #FFFFFF;
  background-color: var(--first-color);
}

/* Light Theme */
.light-theme {
  --first-color: #ffffff;
  color: #292b2c;
  background-color: var(--first-color);
}

/* Background */
.bg-primary {
  background-color: var(--first-color) !important;
}
.bg-secondary {
  background-color: var(--second-color) !important;
}

/* Card */
.card {
  background: hsla(0, 0%, 100%, 1);
  backdrop-filter: blur(30px);
}

/* Title */
.title {
  text-align: center; /* Center align by default */
}

@media (min-width: 1200px) {
  .title {
    float: left; /* Float left when the webpage has sufficient width */
    text-align: left; /* Reset text alignment for float left */
  }
}

/* Buttons */
.btn-primary {
  color: #fff;
  background-color: var(--blue-darkest);
  border-color: var(--blue-darkest);
}

.btn-primary:hover {
  color: #fff;
  background-color: var(--blue-deepest);
  border-color: var(--blue-deepest);
}
```

In the `project/static/jscolorMode.js` we set all the light dark theme (This is optional of course).

```js
function applyTheme() {
  const theme = localStorage.getItem('theme');
  const bodyElement = document.querySelector('body');
  
  if (theme === 'dark') {
    bodyElement.classList.remove('light-theme');
    bodyElement.classList.add('dark-theme');
  } else if (theme === 'light') {
    bodyElement.classList.remove('dark-theme');
    bodyElement.classList.add('light-theme');
  }
}

function toggleTheme() {
  const theme = localStorage.getItem('theme');
  const updatedTheme = theme === 'dark' ? 'light' : 'dark';
  localStorage.setItem('theme', updatedTheme);
  applyTheme();
}

// Set initial theme
document.addEventListener('DOMContentLoaded', applyTheme);
```


IN PROGRESS!
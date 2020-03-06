Guidelines by Bryan Fernandez

for even more assistance, visits the docs:
https://django-mptt.readthedocs.io/en/latest/tutorial.html

poetry init

install the django-mptt package in poetry
install django

poetry install
poetry shell

django-admin startproject *name here
python manage.py createsuperuser

python manage.py makemigrations *name here
python manage.py migrate


*Add mptt to installed apps in settings.py file:

INSTALLED_APPS = (
    'django.contrib.auth',
    # ...
    'mptt',
    'YourProjectNameHere',
)


from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Genre(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']


python manage.py makemigrations <your_app>
python manage.py migrate


{% load mptt_tags %}
<ul>
    {% recursetree genres %}
        <li>
            {{ node.name }}
            {% if not node.is_leaf_node %}
                <ul class="children">
                    {{ children }}
                </ul>
            {% endif %}
        </li>
    {% endrecursetree %}
</ul>

and a simple view to show all Objects
and add a url in urls.py to activate the view method.
from django import template
from django.contrib.auth.models import User, Group

register = template.Library()

def upper(value):
    return User.name

def has_group(User):
    return user.groups.filter(name="Accounting").exists()

register.filter('upper', upper)
register.filter('has_group', has_group)
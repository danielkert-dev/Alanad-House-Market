from django.db import models

from django.dispatch import receiver
from allauth.account.signals import user_signed_up
from allauth.socialaccount.signals import social_account_added

from django.contrib.auth.models import Group

@receiver(user_signed_up)
@receiver(social_account_added)
def add_user_to_group(request, user, **kwargs):
    group_name = 'default'  # Replace with the actual group name

    try:
        group = Group.objects.get(name=group_name)
        user.groups.add(group)
    except Group.DoesNotExist:
        pass

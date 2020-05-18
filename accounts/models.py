from django.db import models
from django.contrib.auth.models import User
from codefuse import settings
from django.urls import reverse
from django.conf import settings


class Developer(models.Model):
    '''A specific type of User - may be a developer or general viewer.'''
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    developer = models.BooleanField(help_text=(
        "Check here if you'd like to be listed as a developer"
    ),
                                     default=False)
    

    def __str__(self):
        '''Return the related User's username.'''
        # type = "Developer" if self.developer is True else "General"
        return f"{self.user.username}'s Profile'"

    def get_absolute_url(self):
        '''Returns a fully qualified path for user profile.'''
        path_components = {'pk': self.user.id} 
        # path_components = {pk=pk}
        return redirect('accounts:user-profile', kwargs=path_components)
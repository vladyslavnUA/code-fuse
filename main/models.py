from django.db import models
# from django.forms import ModelForm
from django.conf import settings
from django.utils.text import slugify
from django.urls import reverse, reverse_lazy

class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=60,
                            blank=True, editable=False,
                            help_text="Unique URL path to access this [property]." +
                                      "Computer Generated.")
    description = models.TextField(help_text="(Elevator Pitch)")
    programming_languages = models.CharField(max_length=200, blank=True)
    frameworks = models.CharField(max_length=400) 
    date_posted = models.DateTimeField(auto_now_add=True, help_text=(
            "The date and time this page was created. " +
            "Automatically generated when the model saves.")
        )
    pub_date = models.DateTimeField(auto_now_add=True, help_text=
            "the date and time this project was posted")
    is_visible = models.BooleanField(help_text="Is currently active?",
                                     default=True)
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  on_delete=models.PROTECT,
                                  null=True, blank=True,
                                  help_text="Posted by: ")

    def __str__(self):
        '''Return the title of the Property for presentation purposes.'''
        return self.title

    def save(self, *args, **kwargs):
        '''Creates a URL safe slug automatically when a new property is made.'''
        if not self.pk:
            self.slug = slugify(self.title, allow_unicode=True)

        # call save on the superclass
        return super(Project, self).save(*args, **kwargs)

    def get_absolute_url(self):
        '''Returns a fully qualified path for building code instance.'''
        path_components = {'slug': self.slug}
        return reverse('projects:details', kwargs=path_components)
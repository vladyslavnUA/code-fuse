from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.urls import reverse, reverse_lazy

class Project(models.Model):
    title = models.CharField(max_length=200, help_text="Project (Working) Title")
    slug = models.CharField(max_length=60,
                            blank=True, editable=False,
                            help_text="Unique URL path to access this [property]." +
                                      "Computer Generated.")
    description = models.TextField(help_text="Think of this as a 1-minute Elevator Pitch")
    date_posted = models.DateTimeField(auto_now_add=True, help_text=(
            "The date and time this page was created. " +
            "Automatically generated when the model saves.")
        )
    pub_date = models.DateTimeField('date published')
    is_visible = models.BooleanField(help_text="Is {} currently active?".format(title),
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
        return super(PropertyItem, self).save(*args, **kwargs)

    def get_absolute_url(self):
        '''Returns a fully qualified path for building code instance.'''
        path_components = {'slug': self.slug}
        return reverse('main:details', kwargs=path_components)
        
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
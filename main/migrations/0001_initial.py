# Generated by Django 3.0.6 on 2020-05-08 19:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Project (Working) Title', max_length=200)),
                ('slug', models.CharField(blank=True, editable=False, help_text='Unique URL path to access this [property].Computer Generated.', max_length=60)),
                ('description', models.TextField(help_text='Think of this as a 1-minute Elevator Pitch')),
                ('date_posted', models.DateTimeField(auto_now_add=True, help_text='The date and time this page was created. Automatically generated when the model saves.')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('is_visible', models.BooleanField(default=True, help_text='Is <django.db.models.fields.CharField> currently active?')),
                ('posted_by', models.ForeignKey(blank=True, help_text='Posted by: ', null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

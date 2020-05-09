from django.urls import path, include
from . import views
from .views import (
    home,
    ProjectList,
    ProjectDetail,
    ProjectCreate,
    ProjectUpdate,
    ProjectDelete,
)

app_name = 'projects'

urlpatterns = [
    path('', views.home, name='home'),
    path('/random', random, name='random'),
    path('projects/', ProjectList.as_view(), name='reference'),
    path('projects/add-project/', ProjectCreate.as_view(), name='add_project'),
    path('projects/<slug:slug>/edit/', ProjectUpdate.as_view(), name='edit_project'),
    path('projects/<slug:slug>/delete/', ProjectDelete.as_view(),
         name='remove_project'),
    path('projects/<slug:slug>/', ProjectDetail.as_view(), name='details'),
]
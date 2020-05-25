from django.shortcuts import render
from django.http import HttpResponseRedirect
from accounts.forms import SignUpForm, StatusForm
from django.urls import reverse, reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from accounts.models import Developer
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.detail import (DetailView)
from django.views.generic.edit import (
    CreateView,
    UpdateView
)
import emoji

class SignUpView(SuccessMessageMixin, CreateView):
    '''Allows site visitors to set up a new account as architect or officer.'''
    form_class = SignUpForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/signup.html'
    success_message = (
        '''Congratulations, You may now log in to Codefuse!
            You now have a user profile :simple_smile: '''
        )

    def form_valid(self, form):
        '''Save the new User, and set up their profile as well.'''
        self.object = form.save()
        developer = Developer.objects.create(
            user=self.object,
            developer=False)
        developer.save()
        return super().form_valid(form)


# class UserProfile(UserPassesTestMixin, DetailView):
    # model = User
    # template_name = 'accounts/profile/show_profile.html'
    # # queryset = User.objects.all()

    # def get_queryset(self):
    #     '''Returns a queryset of all User objects.'''
    #     return self.model.objects.all()

    # def get(self, request, pk):
    #     """Renders a page to show an account of user.
    #        Parameters:
    #        pk(int): specific id of the User in db.
    #        request(HttpRequest): the HTTP request sent to the server
    #        Returns:
    #        render: HttpResponse
    #      """
    #     user = self.get_queryset().get(id=pk)
    #     # developer = user.developer
    #     status = Developer.objects.get(user=user)
    #     context = {
    #         # 'developer': developer,
    #         'user': user,
    #         'status': status,
    #     }
    #     return render(request, self.template_name, context)

    # def test_func(self):
    #     '''Ensures the user can see only their own profile.'''
    #     requested_user = self.get_object()
    #     user = self.request.user
    #     return requested_user == user

class UserProfile(UserPassesTestMixin, DetailView):
    model = User
    template_name = 'accounts/profile/show_profile.html'

    def get_queryset(self):
        '''Returns a queryset of all User objects.'''
        return self.model.objects.all()

    def get(self, request, pk):
        """Renders a page to show an account of user.
           Parameters:
           pk(int): specific id of the User in db.
           request(HttpRequest): the HTTP request sent to the server
           Returns:
           render: HttpResponse
         """
        user = self.get_queryset().get(id=pk)
        status = Developer.objects.get(user=user)
        context = {
            'user': user,
            'status': status
        }
        return render(request, self.template_name, context)

    def test_func(self):
        '''Ensures the user can see only their own profile.'''
        requested_user = self.get_object()
        user = self.request.user
        return requested_user == user

class ProfileUpdate(UserPassesTestMixin, UpdateView):
    model = Developer
    form_class = StatusForm
    template_name = 'accounts/profile/update.html'

    def get_queryset(self):
        '''Returns a queryset of all User objects.'''
        return Developer.objects.all()

    def get(self, request, pk):
        """Renders a page for user to check off if they're a developer or
           general user.
           Parameters:
           pk(int): specific id of the User in db.
           request(HttpRequest): the HTTP request sent to the server
           Returns:
           render: HttpResponse
         """
        status = self.get_queryset().get(id=pk)
        user = User.objects.get(id=status.user.id)
        context = {
            'user': user,
            'status': status
        }
        return super().get(request)

    def test_func(self):
        '''Ensures the user can see only their own profile.'''
        requested_user = self.get_object().user
        user = self.request.user
        return requested_user == user

# def logout_request(request):
#     logout(request)
#     messages.info(request, "Logged out successfully!")
#     return redirect("main:homepage")
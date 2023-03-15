from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.urls import reverse

class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = "users/login.html"
    
    
    def get_success_url(self):
        return reverse("todo:tasks")
    
    def form_invalid(self, form):
        messages.error(self.request,'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form)) 
    

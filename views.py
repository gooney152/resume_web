from django.shortcuts import render
#when a form is valid we want to render a message
from django.contrib import messages
from . models import (
    UserProfile,
    Blog,
    Portfolio,
    Testimonials,
    Certificate
)
from django.views import generic
from . forms import ContactForm

# Create your views here.

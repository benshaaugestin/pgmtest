from django.contrib import admin
from .models import Candidate,Question

admin.site.register(Candidate)
admin.site.register(Question)
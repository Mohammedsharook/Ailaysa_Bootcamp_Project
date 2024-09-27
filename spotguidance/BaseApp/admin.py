from django.contrib import admin
from .models import Category, SubCategory, Spot, ForumComments, Review

admin.site.register([Category,SubCategory,Spot, ForumComments, Review])

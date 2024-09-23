from django.contrib import admin
from .models import Category, SubCategory, Spot, ForumComments, Review
# Register your models here.

admin.site.register([Category,SubCategory,Spot, ForumComments, Review])
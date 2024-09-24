from django.urls import path
from . import views
from . import class_based_views

urlpatterns = [
    path('', views.api_overviews, name='api_overviews'),
    path('Categories/', class_based_views.Category_list.as_view(), name='category_list'),
    path('Subcategories/', class_based_views.Subcategory_list.as_view(), name='subcategory_list'),
    path('Spots/', class_based_views.Spot_details.as_view(), name='spot_list'),


    # Function based view
    # path('Categories/', views.category_list, name='category_list'),
    # path('Subcategories/', views.subcategory_list, name='subcategory_list')
]
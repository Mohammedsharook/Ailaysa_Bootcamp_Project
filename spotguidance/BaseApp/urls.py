from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name='api_overviews'),
    path('Categories/', views.Category_list.as_view(), name='category_list'),
    path('Categories/<int:pk>', views.Category_list.as_view(), name='category_delete'),
    path('Subcategories/', views.Subcategory_list.as_view(), name='subcategory_list'),
    path('Subcategories/<int:pk>', views.Subcategory_list.as_view(), name='subcategory_delete'),
    path('Spots/', views.Spot_list.as_view(), name='spot_list'),
    path('Spot/<int:pk>', views.Spot_detail.as_view(), name='spot_detail'),
    path('Spot-review/<int:pk>', views.Spot_Review_list.as_view(), name='spot_reviews')


    # Function based view
    # path('Categories/', views.category_list, name='category_list'),
    # path('Subcategories/', views.subcategory_list, name='subcategory_list')
]
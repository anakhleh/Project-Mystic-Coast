from django.urls import path
from . import views

app_name = 'campus'
urlpatterns = [
    path('', views.index, name='index'),
    path('add_restaurant_action/', views.add_restaurant_action, name='add_restaurant_action'),
    path('add_restaurant/', views.add_restaurant_page, name='add_restaurant'),
    path('restaurant_list/', views.restaurant_list, name='restaurant_list'),
    path('compare_restaurants/', views.compare_restaurants, name='compare_restaurants'),
    path('compare_restaurants_action/', views.compare_restaurants_action, name='compare_restaurants_action'),
    path('<int:restaurant_id>/', views.restaurant_detail, name='restaurant_detail'),
    path('delete_restaurant_<int:restaurant_id>/', views.delete_restaurant, name='delete_restaurant'),
    path('add_item/', views.add_item, name='add_item'),
    path('load_item/<int:item_id>/<int:restaurant_id>', views.load_item, name='load_item'),
    path('edit_restaurant/<int:restaurant_id>', views.edit_restaurant, name='edit_restaurant'),
    path('user_profile/', views.user_profile, name='user_profile' )
]
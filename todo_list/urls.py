from django.urls import path, include
from . import views
#the array of our url's 
urlpatterns = [
    #our home url, for the main page
    path('', views.home, name="home"),
    #the url for deleting an item 
    path('delete/<list_id>', views.delete, name="delete"),
    #the url for "crossing off" an item 
    path('cross_off/<list_id>', views.cross_off, name="cross_off"),
    #the url for "uncrossing" an item, if you need that item to be shown as not done yet
    path('uncross/<list_id>', views.uncross, name="uncross"),
    #the url for the edit button, which will take you to the edit page
    path('edit/<list_id>', views.edit, name="edit"),
    #these urls have list_id's which are attributes of each item in our to-do list so they can be referenced and are all custom 'views' which come from django's views 
]

#check

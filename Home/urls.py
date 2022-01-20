from re import search
from unicodedata import name
from django.contrib import admin
from django.urls import path,include
from Home import views

# added by anshuman
admin.site.site_header = "Personal Website Admin"
admin.site.index_title = "Welcome Admin"
admin.site.site_title = "Hello Anshu"

urlpatterns = [
    path('',views.index,name='Home'),
    path('projects',views.projects,name='project'),
    # path('experience',views.experience,name="experience"),
    path('blogs',views.blogs,name="blogs"),
    path('search',views.search,name="search"),
]

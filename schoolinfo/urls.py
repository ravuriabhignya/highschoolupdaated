from django.urls import path
from . import views


urlpatterns = [
	path('studentsearch/', views.MainView),
	path('urlsearch/<studentid>/', views.urlsearch),
]
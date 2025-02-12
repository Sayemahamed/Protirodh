from django.urls import path, include

from. import views

urlpatterns = [
    path('create/', views.create_crime_report, name='create_crime_report'),
    path('feed/', views.crime_feed, name='crime_feed'),
    path('detail/<int:report_id>/', views.crime_detail, name='crime_detail'),
    path('vote/<int:report_id>/<int:vote_value>/', views.vote_report, name='vote_report'),
]
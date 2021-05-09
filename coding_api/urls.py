from django.urls import path
from . import views

urlpatterns = [
    path('',views.welcome,name='home'),
    path('list-topics/',views.all_topics,name='all_topics'),
    path('all-mcq/<int:topic_id>/',views.complete_topic,name='complete_topic'),
    path('fill/',views.fill_DB,name='fill'),
]
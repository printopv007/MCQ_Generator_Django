from django.urls import path
from .views import Mcq, RandomQuestion,McqQuestion
from django.conf import settings
from django.conf.urls.static import static

app_name='mcq'

urlpatterns= [
    path('',Mcq.as_view(),name='mcq'),
    path('r/<str:topic>/',RandomQuestion.as_view(),name='RandomQuestion'),
    path('q/<str:title>/',McqQuestion.as_view(),name='mcq'),
] +static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
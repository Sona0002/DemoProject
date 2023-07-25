from . import views
from django.urls import path

urlpatterns = [

    path('', views.demo, name='demo'),
    path('operation/', views.operation, name='operation'),
    # path('add/',views.addition,name='addition'),
    # path('sub/',views.subtraction,name='subtraction'),
    # path('mul/',views.multiplication,name='multiplication'),
    # path('div/',views.division,name='division'),
    # path('about/',views.about,name='about'),
    # path('contact/',views.contact,name='contact'),
    # path('details/',views.details,name='details'),
    # path('thanks/',views.thanks,name='thanks')
]


from django.urls import path
from . import views

urlpatterns=[
    path('',views.rooms,name='rooms'),
    path('create/',views.createrooms,name='create'),
    path('quick/',views.quickjoin,name='quick'),
    path('delete/',views.deleterooms,name='delete'),
    path('<slug:slug>/',views.room,name='room'),
]


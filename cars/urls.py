from django.urls import path
from . import views
from comments import views as comment_views

app_name = 'cars'

urlpatterns = [
    path('', views.index, name='index'),
    path('new', views.new, name='new'),
    path('add', views.add, name='add'),
    path('<pk>/edit', views.edit, name='edit'),
    path('<pk>/delete', views.delete, name='delete'),
    path('<pk>/comment', comment_views.create, name='comment'),
    path('<pk>/', views.show, name='show'),
]
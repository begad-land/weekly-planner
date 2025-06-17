
from . import views
from django.urls import path

urlpatterns = [
    path('home' , views.Main.as_view() , name = 'home'),
    path('delete/<int:task_id>/' , views.DeleteTask.as_view() , name = 'delete'),
    path('update/<int:task_id>/' , views.UpdateTask.as_view() , name = 'update'),

]


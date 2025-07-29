
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.signup),
    path('signin/', views.signin),
    path('todo/', views.todo),
    path('edit_todo/<int:id>', views.edit_todo , name='edit_todo'),
    path('delete_todo/<int:id>', views.delete_todo, name='delete_todo'),
    path('signout/', views.signout, name ='signout'),
    

   

]

"""
URL configuration for todo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tasks import views as task_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', task_views.task_list, name='task_list'),
    path('api/tasks/add', task_views.add_task_api, name='add_task_api'),
    path('add/input', task_views.add_task_input, name='add_task_input'),
    path('categories/add/input', task_views.categories_add_input, name='categories_add_input'),
    path('api/categories/add', task_views.add_categories_api, name='add_categories_api'),
    path('api/tasks/delete/<int:task_id>', task_views.delete_task_api, name='delete_task_api'),
    path('tasks/edit/<int:task_id>', task_views.edit_task_input, name='edit_task_input'),
    path('api/tasks/edit/<int:task_id>', task_views.edit_task_api, name='edit_task_api'),
]

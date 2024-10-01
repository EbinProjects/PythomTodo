from django.urls import path, include
from . import views

urlpatterns = [

    # path('Details', views.AllTasks, name='AllTasks'),
    path('', views.Todo, name='TodoP'),
    path('delete/<int:tackid>', views.Delete, name='Delete'),
    path('update/<int:tackid>', views.update, name='Update'),
    path('cbvHome/', views.TodoListView.as_view(), name='cbvHome'),
    path('cbvAdd/', views.Todo, name='cbvAdd'),
    path('cbDetails/<int:pk>', views.Details.as_view(), name='cbDetails'),
    path('cbUpdate/<int:pk>', views.TaskUpdate.as_view(), name='cbUpdate'),
    path('cbDelete/<int:pk>', views.Deleted.as_view(), name='Deleted')
]

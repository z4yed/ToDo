
from django.urls import path, include
from .views import homeView, detailView, createView, editView,deleteView, completedView, markComplete, welcome

urlpatterns = [

    path('', welcome, name="welcome-view"),
    path('view/', homeView, name = 'home-view'),
    path('create/', createView, name = 'create-view'),
    path('todo/<int:pk>/', detailView, name = 'detail-view'),
    path('todo/<int:pk>/edit/', editView, name='edit-view'),
    path('todo/<int:pk>/delete/', deleteView, name="delete-view"),
    path('todo/completed/', completedView, name = 'completed-view'),
    path('todo/<int:pk>/complete', markComplete, name = 'complete-todo'),

]

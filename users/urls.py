from django.urls import path, include
from .views import user_signup


urlpatterns = [

        path('signup/', user_signup, name='user-signup'),

]

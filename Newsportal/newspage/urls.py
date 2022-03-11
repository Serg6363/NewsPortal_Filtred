from django.urls import path
from .views import PostList, PostText


urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>', PostText.as_view()),
]

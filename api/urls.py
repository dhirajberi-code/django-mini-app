from django.urls import path
from .views import PostList, PostDetail

urlpatterns = [
    path('<int:pk>/', PostDetail.as_view()),
    path('', PostList.as_view()),
]

'''
All blog routes will be at api/v1/ so our PostList view has the empty string '' will be at api/v1/ and the PostDetail view at api/v1/# where #
represents the primary key of the entry. For example, the first blog post has a primary id of 1 so
it will be at the route api/v1/1, the second post at api/v1/2, and so on.
'''
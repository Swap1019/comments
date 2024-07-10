from django.urls import path,include
from .views import BlogView,Reply

app_name = 'comments'

urlpatterns = [
    path('test/<int:pk>',BlogView.as_view(),name='test'),
    path('replyto/<int:blog_id>/<int:comment_id>',Reply.as_view(),name='reply')
]
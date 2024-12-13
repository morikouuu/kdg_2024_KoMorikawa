from django.urls import path,include
from . import views

app_name = 'blogs'
urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:pk>', views.BlogDetailView.as_view(), name = 'detail'),
    path('create/', views.CreateView.as_view(), name='create'),
    path('delete/<int:pk>/',views.DeleteView.as_view(),name = 'delete'),
    path('update/<int:pk>/',views.UpdateView.as_view(),name = 'update'),
    path('commentcreate/<int:pk>/',views.CommentCreateView.as_view(),name = 'commentcreate'),
    path('detail/<int:blog_id>/comment/<int:comment_id>/', views.CommentDetailView.as_view(), name='commentdetail'),
    
    path('comment/<int:pk>/', views.comment_create, name='comment_create'),
    path('reply/<int:comment_id>/', views.reply_create, name='reply_create'),
] 
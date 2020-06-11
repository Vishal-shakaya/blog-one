from post import views 
from django.urls import path , include 
app_name = 'Post'
urlpatterns =[
path('post-create/',views.PostCreat.as_view(),name='create'),
path('post-edit/<int:pk>',views.PostUpdate.as_view(),name='update'),
path('post-list/',views.PostList.as_view(),name='post_list'),
path('post-detail/<pk>/',views.PostDetail.as_view(),name='detail'),
path('post-delete/<int:pk>/',views.PostDelete.as_view(),name='delete'),
path('publish-post/<int:pk>/',views.publish_post,name='publish'),

]
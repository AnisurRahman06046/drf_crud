from django.urls import path
from . import views


urlpatterns=[
    path('create/',views.createBlog,name='createBlog'),
    path("all-blogs/",views.allBlogs,name='allBlogs'),
    path("blog-detail/<str:id>/",views.singleBlog),
    path("blog/update/<str:id>",views.updateBlog),
    path("delete/<str:id>",views.deleteBlog)
]
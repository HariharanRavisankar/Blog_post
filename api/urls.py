from django.urls import path , include
from . import views

urlpatterns =[
    path("blogpost/",views.BlogPostListCreate.as_view(), name="blogpost-view-create"),
    path("blogpost/<int:pk>/", views.BLogPostRetriveUpdateDestroy.as_view(), name="update"),
]
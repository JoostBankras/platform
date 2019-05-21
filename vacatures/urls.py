from django.urls import path
# from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from . import views
from django.views.generic import TemplateView
from .views import VacaturesListView, VacatureCreateView, VacatureDetailView, VacatureUpdateView, VacatureDeleteView
 
urlpatterns = [
    # path('', TemplateView.as_view(template_name='vacatures/homepage.html'), name='homepage'),
    path('', VacaturesListView.as_view(), name="vacatures"),
    path('new/', VacatureCreateView.as_view(), name="vacatures-create"),
    path('<int:pk>/', VacatureDetailView.as_view(), name="vacature-detail"),
    path('<int:pk>/update/', VacatureUpdateView.as_view(), name="vacature-update"),
    path('<int:pk>/delete/', VacatureDeleteView.as_view(), name="vacature-delete"),
    path('<int:pk>/react/', views.add_reaction, name="add_reaction"), 
    # path('', PostListView.as_view(), name="blog-home"), 
    # path('user/<str:username>', UserPostListView.as_view(), name="user-posts"),
    # path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    # path('post/new/', PostCreateView.as_view(), name="post-create"),
    # path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post-update"),
    # path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post-delete"),
    # path('about/', views.about,name="blog-about"),
]
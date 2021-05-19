from django.urls import path
from . import views
from .views import blog_category, PostDashboardView
#from .feeds import LatestPostsFeed
#from marketing.views import email_list_signup

urlpatterns = [
    #path('', views.home, name='home'),
    path('dashboard/', PostDashboardView.as_view(), name='post-dashboard'),
    path('category/<slug:category_slug>/', views.blog_category, name='categories'),
    path('listings/', views.listings, name='listings'),
    path('tag/<slug:tag_slug>',views.listings, name='listings_by_tag'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('search', views.search, name='search'),
    #path('subscribe/', email_list_signup, name="subscribe"),
    #path('feed/',LatestPostsFeed(),name='post_feed'),
]

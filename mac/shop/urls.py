
from django.urls import path
from . import views
urlpatterns = [
    path("", views.index,name="ShopHome"),
    path("about/", views.about,name="about"),
    path("contact/", views.contact,name="ContactUs"),
    path("tracker/", views.tracker,name="Tracking Status"),
    path("search/", views.search,name="Search"),
    path("productview/", views.prodView,name="Product View"),
    path("checkout/", views.checkout,name="Checkout"),

]

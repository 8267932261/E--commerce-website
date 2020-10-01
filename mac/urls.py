
from django.urls import path
from . import views #import this

urlpatterns = [
    path('',views.index,  name ='shophome'),
    path('about/',views.about,  name ='Aboutus'),
    path('contact/',views.contact,  name ='Contactus'),
    path('tracker/',views.tracker,  name ='Trackeringstatus'),
    path('search/',views.search,  name ='Search'),
    path("products/<int:myid>", views.productView, name="ProductView"),
    path('checkout/',views.checkout,  name ='checkout'),
    
    
    
]
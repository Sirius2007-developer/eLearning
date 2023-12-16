from django.urls import path
from .views import index, a404, contact, about, courses, team, testimonial, carouseldetailview, read, coursedetailview

urlpatterns = [
    path('', index, name="index"),
    path('a404/', a404, name="a404"),
    path('contact/', contact, name="contact"),
    path('about/', about, name="about"),
    path('courses/', courses, name="courses"),
    path('team/', team, name="team"),
    path('testimonial/', testimonial, name="testimonial"),
    path('caro/<int:id>/', carouseldetailview, name="carodetail"),
    path('read/', read, name="read"),
    path('cour/<int:id>/', coursedetailview, name="coursedetail"),
]
from django.urls import path
from .views import *




urlpatterns = [
    path('index/',index),
    path('login/',login),
    path('register/',register),
    path('footer/',footer),
    path('navbar/',navbar),
    path('profile/',profile),
    path('testimonials/',testimonials),
    path('about/',about),
    path('terms/',terms),
    path('samplenavbar/',samplenavbar),
    path('contact/',contact),
    path('vaccancyupload/<int:id>',vaccancyupload),
    path('vaccancysuccess/',vaccancysuccess),
    path('vaccancyedit/<int:id>',vaccancyedit),
    path('vaccancydelete/<int:id>',vaccancydelete),
    path('userregistration/',userregistration),
    path('userlogin/', userlogin),
    path('userdetails/<int:id>',userdetails),
    path('userprofile/',userprofile),
    path('userviewvaccancy/',userviewvaccancy),
    path('userdisplay/',userdisplay),
    path('userdetailsedit/<int:id>',userdetailsedit),
    path('userdetailsdelete/<int:id>',userdetailsdelete),
    path('editcompanyprofile/<int:id>',editcompanyprofile),
    path('jobapply/<int:id>',jobapply),
    path('applysuccess/',applysuccess),
    path('wishlist/<int:id>',wishlist),
    path('mywish/',mywish),
    path('removewish/<int:id>',removewish),
    path('viewappliedusers/',viewappliedusers),
    path('success/',success),
    path('email/<int:id>',email),
    path('removeapply/<int:id>',removeapply),
    path('viewcompanies/',viecompanies)





]
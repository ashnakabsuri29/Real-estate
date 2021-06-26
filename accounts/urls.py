from django.urls import path , include
from django_email_verification import urls as email_urls
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('register1',views.register1,name='register1'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('search',views.search,name='search'),
    path('index',views.index,name='index'),
    path('detail/<int:id>',views.detail,name='detail'),
    path('sell',views.sell,name='sell'),
    path('contact',views.contact,name='contact'),
    path('detail/enquiry/<int:id>',views.enquiry,name='enquiry'),
    path('detail/enquiry/enquiry_confirmation',views.enquiry_confirmation,name='enquiry_confirmation'),
    path('email/', include(email_urls)),
   
]


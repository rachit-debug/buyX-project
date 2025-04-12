from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
path('local/', admin.site.urls),
path('',views.indexpage,name='indexpage'),
path('myaddtocart', views.myaddtocart, name='myaddtocart'),
path('about',views.about,name='about'),
path('service',views.service,name='service'),
path('team',views.team,name='team'),
path('contact',views.contact,name='contact'),
path('myaboutpage',views.myaboutpage,name='myaboutpage'),

path('project',views.project,name='project'),
path('submitquery',views.submitquery,name='submitquery'),
path('quotedata',views.quotedata,name='quotedata'),
path('loginpage',views.loginpage,name='loginpage'),
path('login',views.login,name='login'),
path('createaccount',views.createaccount,name='createaccount'),
path('logout',views.logout,name='logout'),  
path('productview/<int:myid>',views.productview,name='productview'),
path('myaddtocart',views.myaddtocart,name='myaddtocart'),
path('productview/myaddtocart',views.myaddtocart,name='myaddtocart'),
path('mycart',views.mycart,name='mycart'), 
path('productview/mycart',views.mycart,name='mycart'),
path('clearcart',views.clearcart,name='clearcart'),
path('myaddtocarttcart',views.myaddtocarttcart,name='myaddtocarttcart'),
path('myaddtocartcart',views.myaddtocartcart,name='myaddtocartcart'),
path('removecatitem',views.removecatitem,name='removecatitem'),
path('userprofile',views.userprofile,name='userprofile'),
path('myorders',views.myorders,name='myorders'),
path('blogone',views.blogone,name='blogone'),
path('blogtwo',views.blogtwo,name='blogtwo'),
path('blogthree',views.blogthree,name='blogthree'),
# path('productsearch',views.productsearch,name='productsearch'), 
path('mycart',views.mycart,name='mycart'), 
# password
 path('changepassword',views.changepassword,name='changepassword'),
    path('changepassword2',views.changepassword2,name='changepassword2'),
    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"), 
        name="password_reset_complete"),
path('paynow/', views.paynow, name='paynow'),
path('paymentpolicy', views.paymentpolicy, name='paymentpolicy'),
path('refundpolicy', views.refundpolicy, name='refundpolicy'),
path('cancelpolicy', views.cancelpolicy, name='cancelpolicy'),
path('allproducts/', views.allproducts, name='allproducts'),
path('allproducts/productview/<int:myid>',views.productview,name='productview'),
path('premium',views.premium, name='premium'),








]
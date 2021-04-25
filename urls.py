
from django.urls import path
from .import views

urlpatterns = [

    path('',views.home,name='home'),
    path('login',views.login,name='login'),
    path('log',views.log,name='log'),
    path('home',views.home,name='home'),
    path('ureg', views.ureg, name='ureg'),
    path('reg', views.reg, name='reg'),
    path('uhome',views.uhome,name='uhome'),
    path('registration',views.registration,name='registration'),
    path('memberreg',views.memberreg,name='memberreg'),
    path('memreg', views.memreg, name='memreg'),
    path('activityreg',views.activityreg,name='activityreg'),
    path('actreg', views.actreg, name='actreg'),
    path('productreg',views.productreg,name='productreg'),
    path('proreg', views.proreg, name='proreg'),
    path('show', views.show, name='show'),
    path('productdetails', views.productdetails, name='productdetails'),

    path('editadminpro', views.editadminpro, name='editadminpro'),
    path('update1', views.update1, name='update1'),
    path('memberdetails', views.memberdetails, name='memberdetails'),
    path('memberdetails1', views.memberdetails1, name='memberdetails1'),
    path('addingstock', views.addingstock, name='addingstock'),
    path('adstock', views.adstock, name='adstock'),
    path('ad1stock', views.ad1stock, name='ad1stock'),
    path('uprodetails', views.uprodetails, name='uprodetails'),
    path('viewcustprofile', views.viewcustprofile, name='viewcustprofile'),
    path('search', views.search, name='search'),
    path('sear', views.sear, name='sear'),
    path('editcustprofile', views.editcustprofile, name='editcustprofile'),
    path('update', views.update, name='update'),
    path('actentry', views.actentry, name='actentry'),
    path('acte', views.acte, name='acte'),
    path('mhome', views.mhome, name='mhome'),
    path('mprodetails', views.mprodetails, name='mprodetails'),
    path('viewmemprofile', views.viewmemprofile, name='viewmemprofile'),
    path('loan', views.loan, name='loan'),
    path('logout', views.logout, name='logout'),
    path('cart1', views.cart1, name='cart1'),
    path('gocart', views.gocart, name='gocart'),
    path('cartdetails', views.cartdetails, name='cartdetails'),
    path('shopping', views.shopping, name='shopping'),

]
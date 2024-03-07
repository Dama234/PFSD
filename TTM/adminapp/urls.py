from django.urls import path
from . import views

urlpatterns = [
    path("checkadminlogin",views.checkadminlogin, name="checkadminlogin"),
    path("checkregistration",views.checkregistration, name="checkregisteration"),
    path("checkpackages",views.checkpackages,name="checkpackages"),
    path("viewplaces",views.viewplaces,name="viewplaces"),
    path("changepassword",views.checkChangePassword,name="changepassword"),
    path("logout",views.logout,name="logout"),
path('random1',views.random1,name='random1'),
path('randomotp',views.randomotp,name='randomotp'),

]
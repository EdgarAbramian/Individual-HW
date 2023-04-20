"""
URL configuration for TraidingBot project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path
from TradeApp.views import index_page,auto,rec_cur,rec_buy,rec_sell,get_cur
# from TradeApp.views import topcoin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page,name ='home'),
    path('auto', auto,name = 'auto'),
    path('rec_cur', rec_cur,name = 'rec_cur'),
    path('rec_buy', rec_buy,name = 'rec_buy'),
    path('rec_sell', rec_sell,name = 'rec_sell'),
    path('get_cur', get_cur,name = 'get_cur'),
    # path('auto', topcoin, name='ex'),

]

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import UserTenderlistview,regusertender,mybiddings,userhome,confirmedbiddings,uprofile
from django.contrib.auth import views as auth_views

app_name='user'
urlpatterns = [
    path('',userhome),
    path('uprofile/',uprofile,name="uprofile"),
    path('tenderlist/',UserTenderlistview.as_view(),name="user-tender-list"),
    path('registerusertender/<str:tendername>/<str:contractorname>/<int:baseprice>/',regusertender),
    path('mybiddings/',mybiddings,name='userbiddings'),
    path('confirmedbiddings',confirmedbiddings,name="confirmed_biddings"),
    path('logout/',auth_views.LogoutView.as_view(template_name='contractor/logout.html'),name='ulogout'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
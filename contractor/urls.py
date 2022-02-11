from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .views import registertender,regsuccess,tenderlist,contractorhome,allbiddings,confirmbiddings,profile

urlpatterns = [
    path('',contractorhome),
    path('profile/',profile,name="profile"),
    path('registertender/',registertender,name='register-tender'),
    path('regsuccess/',regsuccess),
    path('tenderlist/',tenderlist,name="tender-list"),
    path('allbiddings/',allbiddings,name="allbiddings"),
    path('confirmbiddings/<str:tendername>/<str:username>/<int:bidprice>/',confirmbiddings,name="confirmbiddings"),
    path('logout/',auth_views.LogoutView.as_view(template_name='contractor/logout.html'),name='logout'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.urls import path, include
from leads.views import home_page, landing_page, SignupView, RegisterVenderUser
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page, name="landing_page" ),
    path('login/',LoginView.as_view(), name="login"),
    path('logout/',LogoutView.as_view(), name="logout"),  
    path('signup/', SignupView.as_view(), name="signup"),
    path('vender-signup/',RegisterVenderUser, name="vender-registration"),
    path('leads/', include('leads.urls', namespace="leads")),
    path('produits/', include('produits.urls', namespace="produits")),
    path('commandes/', include('commande.urls', namespace="commande")),
    path('my-company/', include('mycompany.urls', namespace='mycompary')),
   
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


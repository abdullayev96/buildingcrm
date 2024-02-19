from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import settings
from django.conf.urls.static import static


urlpatterns = [
    path('noxontrade/', admin.site.urls),
    path('', include("good.urls")),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

##### not_trade
#### 12345
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from artwork.views import auth, EntryViewSet, EntryView

router = SimpleRouter()

router.register(r'entry', EntryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url('', include('social_django.urls', namespace='social')),
    path('', auth),
    path('accounts/profile/', EntryView.as_view()),
]

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




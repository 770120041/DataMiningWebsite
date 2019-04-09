from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    # this line redirects empty to polls
    path('', RedirectView.as_view(url='/polls/', permanent=True)),
    path('polls/', include(('polls.urls', 'polls'), namespace='polls')),
    path('admin/', admin.site.urls),
]
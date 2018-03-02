# -*- encoding: utf-8 -*-
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^quality-global/', include('bar_codes.urls', namespace='bar_codes')),
    url(r'^$', RedirectView.as_view(url=reverse_lazy('bar_codes:generated')), name='index'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns

from allauth.account.views import PasswordResetView

urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),
    path("admin/", admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('accounts/password/reset/', PasswordResetView.as_view(), name='password_reset'),

    path("", include("core.urls")),
    path("", include("pages.urls")),
    re_path(r'^rosetta/', include('rosetta.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# for url patterns domain/language/uri/
# urlpatterns += i18n_patterns(
#     path('accounts/', include('allauth.urls')),
#     path('accounts/password/reset/', PasswordResetView.as_view(), name='password_reset'),

#     path("", include("core.urls")),
#     prefix_default_language=False,
# ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # Examples:
    # url(r'^$', 'assignments2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    path('admin/', admin.site.urls),
    path("", include('register.urls'))
]

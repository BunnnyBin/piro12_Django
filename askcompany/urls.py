from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls')),
    path('blog/', include('blog.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [   # += : 기본 url 삭제되지 않고 추가되도록
        path('__debug__/', include(debug_toolbar.urls)),
    ]


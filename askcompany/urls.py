from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls')),
    path('blog/', include('blog.urls')),
]
# url 클릭하면 해당 이미지 보이게끔
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [   # += : 기본 url 삭제되지 않고 추가되도록
        path('__debug__/', include(debug_toolbar.urls)),
    ]


from django.urls import path, include
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('gogetthegood/', views.gogetthegood, name="good"),
    path('happyhappyjoyjoy/', views.happyhappyjoyjoy, name="happy")
]


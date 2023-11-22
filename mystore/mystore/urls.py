"""
URL configuration for mystore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path
from rest_framework.routers import SimpleRouter

from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from comicstore.views import *    



router = SimpleRouter()

# router.register('api/product', ProductList)
router.register('books', ProductList)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/product/', include(router.urls)),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/drf_auth/', include('rest_framework.urls')), #сессия по cookies
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/product/sign_up/', UserCreateViewSet.as_view()), # UserCreateViewSet.as_view({"post":"create", "delete":"destroy"}) "get": "retrieve", "put": "update" # без указания параметров в скобке, возникала ошибка. The problematic part is when ThingView uses e.g. ModelViewSet or another viewset with default actions defined. It would be nice if the patch for #2171 would take the type of view in consideration and if actions is None default to the actions that exist in the viewset by default. It currently appears that we need to solve the problem this way, passing actions dictionaries for a viewset with default actions set because actions is not permitted to be None and does not default to the default values of the view:
    path('api/product/userinfo/', UserInfoViewSet.as_view({'get':'list'})),
]


urlpatterns += router.urls


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/product/', ProductAPIList.as_view()),
# ]

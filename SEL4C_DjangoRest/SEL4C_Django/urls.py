from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from SEL4C_Django.sel4c import views
from drf_spectacular.views import SpectacularAPIView
from drf_spectacular.views import SpectacularRedocView, SpectacularSwaggerView
from drf_spectacular.views import SpectacularAPIView
from rest_framework_simplejwt import views as jwt_views


router = routers.DefaultRouter()
""" router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet) """

router.register(r'usuarios', views.UserViewSet)
router.register(r'entrepreneurs', views.EntrepreneurViewSet)
router.register(r'activities', views.ActivityViewSet)
router.register(r'files', views.FileViewSet)
router.register(r'questions', views.QuestionViewSet)
router.register(r'answers', views.AnswerViewSet)


urlpatterns = [
  path('api-root/', include(router.urls)),
  path('api-auth/', include('rest_framework.urls', namespace= 'rest_framework')),
  path("admin/", admin.site.urls),
  
  #OpenApi
  path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
  # Swagger UI:
  path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
  # Redoc UI:
  path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

  path("home/",views.HomeView.as_view(), name= "home"),
  path("users/<int:id>/", views.EntrepreneurView.as_view(), name= "user_page"),
  #path('', include('django.contrib.auth.urls')),
  path('',views.LoginView.as_view(), name= "login"),
  path('logout', views.logoutView, name = "logout"),

  path('register/', views.registerUser, name='register'),

  path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]

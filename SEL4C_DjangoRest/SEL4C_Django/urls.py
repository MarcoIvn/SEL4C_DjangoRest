from django.contrib import admin
from django.contrib.auth.decorators import login_required
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

router.register(r'entrepreneurs', views.EntrepreneurViewSet)
router.register(r'activities', views.ActivityViewSet)
router.register(r'files', views.FileViewSet)
router.register(r'questions', views.QuestionViewSet)
router.register(r'answers', views.AnswerViewSet)
router.register(r'completed-acts', views.ActivitiesCompletedViewSet)


urlpatterns = [
  #path('', include('django.contrib.auth.urls')),
  path('api-root/', include(router.urls)),
  path('api-auth/', include('rest_framework.urls', namespace= 'rest_framework')),
  path("admin/", admin.site.urls),
  
  #OpenApi
  path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
  # Swagger UI:
  path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
  # Redoc UI:
  path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
  path('api/answers/create-multiple/', views.CreateMultipleAnswersView.as_view(), name='create-multiple-answers'),
  path('api/questions/create-multiple/', views.CreateMultipleQuestionsView.as_view(), name='create-multiple-questions'),


  path('',views.LoginView.as_view(), name= "login"),
  path('logout', views.logoutView, name = "logout"),

  path('register/', views.registerAdministrator.as_view(), name='register_administrator'),
  path('delete/<int:pk>/', login_required(views.AdministratorDeleteView.as_view(), login_url='login'), name='delete_administrator'),
  path('<int:pk>/password/', login_required(views.changeAdministratorPassword,login_url='login'), name='password' ),

  path('profile/', login_required(views.editAdministrator), name='profile' ),
  
  path('eliminar-administrador/<int:id>/', views.deleteOneAdministrator, name='delete_one_administrator'),
  path('home/administradores/editar-administrador/<int:id>/', views.editOneAdministrator, name='edit_one_administrator'),
  path('home/administradores/<int:id>/password/', views.changeOneAdministratorPassword, name='change_one_administrator_password'),
  
  path("home/",views.HomeView.as_view(), name= "home"),

  path('home/administradores/', login_required(views.AdministratorsView.as_view(), login_url='login'), name= 'administrators'),
  path('home/administradores/<int:id>/', login_required(views.AdministratorView.as_view(), login_url='login'), name= 'administrator'),

  path("entrepreneurs/<int:id>/", views.EntrepreneurView.as_view(), name= "entrepreneur_page"),
  
  # JWT Authentication
  path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
  path('api/token/verify/', jwt_views.TokenVerifyView.as_view(), name='token_verify'),
  
  #OpenApi
  path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
  # Swagger UI:
  path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
  # Redoc UI:
  path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
  
  path('file/<int:file_id>/', views.download_file, name='download-file'),

  path('files/', login_required(views.fileList, login_url='login'), name='files'),
  path('entrepreneurs/', login_required(views.listOfEntrepreneurs, login_url='login'), name='entrepreneurs_list'),
  path('activities/',login_required(views.activityList, login_url='login'), name='activities'),
  path('activities/<int:pk>', login_required(views.ActivityUpdateView.as_view(), login_url='login'), name='update_activity'),
  path('activities/create', login_required(views.ActivityCreateView.as_view(), login_url='login'), name='create_activity'),
  
  path('questions/',login_required(views.questionList, login_url='login'), name='questions'),
  path('questions/<int:pk>', login_required(views.QuestionUpdateView.as_view(), login_url='login'), name='update_question'),
  path('questions/create', login_required(views.QuestionCreateView.as_view(), login_url='login'), name='create_question'),

  path('csv/answers/',login_required(views.csv_all_entrepreneurs_answers, login_url='login'), name='csv_all_answers'),
  path('csv/answers/<int:id>',login_required(views.csv_one_entrepreneur_answers, login_url='login'), name='csv_one_answers'),
  path('csv/answers/<int:id>/<int:activity>',login_required(views.csv_one_entrepreneur_act_answers, login_url='login'), name='csv_one_act_answers'),
]
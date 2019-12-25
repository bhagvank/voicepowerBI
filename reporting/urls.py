from django.urls import path

from . import views
from django.conf.urls.static import static
from voice import settings


app_name = 'reporting'
urlpatterns = [
   
  #  path('', views.IndexView.as_view(), name='index'), 
    #path('', views.home, name='index'), 
    path('', views.login, name='login'),
    path('authenticate/', views.authenticate, name='authenticate'), 

    path('register/', views.register, name='register'),
    path('main', views.main, name='main'),
    path('resume', views.resume, name='resume'),
    path('saveProfile/', views.SaveProfile, name='save'), 
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'), 
    path('voice/', views.voice, name='voice'),
    path('voiceinput/', views.voiceinput, name='voiceinput'),
    # ex: /polls/5/
    #path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    #path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    #path('<int:question_id>/vote/', views.vote, name='vote'),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

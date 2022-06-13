from django.urls import path
from . import views

urlpatterns = [
    path('<int:apno>/<str:pat_name>/<str:doc_name>/', views.peer, name='peer'),
    path('peer1/', views.peer1, name='peer1'),
    path('peer2/', views.peer2, name='peer2'),
    path('fileupload/<int:apno>/<str:doc_name>/<str:pat_name>/',views.fileUpload, name='fileupload')
]
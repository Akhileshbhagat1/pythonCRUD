# from django.urls import path
# from . import views
#
# app_name = 'employee_register'
#
# urlpatterns = [
#     path('subjects/', views.SubjectListView.as_view(),
#          name='subject_list'),
#     path('subjects/<pk>/', views.SubjectDetailView.as_view(),
#          name='subject_detail')
#
# ]

from rest_framework.routers import SimpleRouter
from .views import SubjectListView


router = SimpleRouter()
router.register('posts', SubjectListView)
urlpatterns = router.urls

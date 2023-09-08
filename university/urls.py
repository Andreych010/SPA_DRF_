from django.urls import path

from university.apps import UniversityConfig
from rest_framework.routers import DefaultRouter
from university.views import *

app_name = UniversityConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
                  path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
                  path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),
                  path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_retrieve'),
                  path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
                  path('lesson/destroy/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson_destroy'),

                  path('payments/', PaymentsListApiView.as_view(), name='payments_list'),
                  path('payments/create/', PaymentsCreateApiView.as_view(), name='payments_list'),
                  path('payments/<int:pk>/', PaymentsRetrieveApiView.as_view(), name='payments_retrieve'),
                  path('payments/update/<int:pk>/', PaymentsUpdateAPIView.as_view(), name='payments_update'),
                  path('payments/destroy/<int:pk>/', PaymentsDestroyAPIView.as_view(), name='payments_destroy'),
              ] + router.urls

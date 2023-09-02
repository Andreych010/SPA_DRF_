from django.urls import path

from university.apps import UniversityConfig
from rest_framework.routers import DefaultRouter
from university.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, \
    LessonUpdateAPIView, LessonDestroyAPIView

app_name = UniversityConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')
# router.register(r'lessons', LessonViewSet, basename='lessons')

urlpatterns = [
                  path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
                  path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),
                  path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_retrieve'),
                  path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
                  path('lesson/destroy/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson_destroy'),

              ] + router.urls

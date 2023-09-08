from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework import viewsets, generics, serializers
from university.serializer import *


class CourseViewSet(viewsets.ModelViewSet):
    # serializer_class = CourseSerializer
    queryset = Course.objects.all()
    default_serializer = CourseSerializer
    serializers = {
        'list': CourseSerializer,
        'retrieve': CourseDetailSerializer
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    # queryset = Lesson.objects.all()


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDestroyAPIView(generics.DestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class PaymentsListApiView(generics.ListAPIView):
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('lesson', 'course', 'method_payment')
    ordering_fields = ('date_payment',)


class PaymentsCreateApiView(generics.CreateAPIView):
    serializer_class = PaymentsSerializer
    # queryset = Lesson.objects.all()


class PaymentsRetrieveApiView(generics.RetrieveAPIView):
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()


class PaymentsUpdateAPIView(generics.UpdateAPIView):
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()


class PaymentsDestroyAPIView(generics.DestroyAPIView):
    serializer_class = PaymentsSerializer
    queryset = Lesson.objects.all()

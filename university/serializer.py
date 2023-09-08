from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from university.models import Course, Lesson, Payments


class LessonSerializer(serializers.ModelSerializer):
    course = SlugRelatedField(slug_field='name_course', queryset=Course.objects.all())

    class Meta:
        model = Lesson
        fields = '__all__'


class LessonDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    # lesson_key = LessonSerializer(many=True)
    num_lesson = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_num_lesson(self, obj):
        if obj.lesson_key.all().count():
            return obj.lesson_key.all().count()
        return 0


class CourseCreateSerializer(serializers.Serializer):
    lesson_set = LessonSerializer(source='lesson_set', many=True, allow_null=True)

    def create(self, validated_data):
        lessons_data = validated_data.pop('lesson_set')
        course = Course.objects.create(**validated_data)
        if lessons_data:
            for lesson in lessons_data:
                Lesson.objects.create(**lesson, course=course)
        return course


class CourseDetailSerializer(serializers.ModelSerializer):
    num_lesson = serializers.SerializerMethodField()
    lesson = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_num_lesson(self, obj):
        if obj.lesson_key.all().count():
            return obj.lesson_key.all().count()
        return 0

    def get_lesson(self, course):
        return LessonSerializer(Lesson.objects.filter(course=course), many=True).data


class PaymentsSerializer(serializers.ModelSerializer):
    course = SlugRelatedField(slug_field='name_course', queryset=Course.objects.all())

    class Meta:
        model = Payments
        fields = '__all__'

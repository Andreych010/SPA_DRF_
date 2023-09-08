from django.contrib import admin

from users.models import User
from university.models import Lesson, Course, Payments


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'surname', 'email', 'avatar', 'phone', 'side',)
    search_fields = ('surname',)


@admin.register(Course)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_course', 'preview_course', 'description',)
    search_fields = ('name_course',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_lesson', 'description', 'link_video', 'preview_lesson',)
    search_fields = ('name_lesson',)

    # def lesson_link(self, obj):
    #     if obj.link_video:
    #         return "<a href='%s'>Link</a>" % obj.link_video
    #     else:
    #         return ''


@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'course', 'lesson', 'client', 'date_payment', 'amount_payment', 'method_payment',)
    search_fields = ('client',)

from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from django.core.management import BaseCommand

from university.models import Lesson, Course


class Command(BaseCommand):
    def handle(self, *args, **options):
        # user_johndoe = User.objects.create(surname="johndoe", email='marchuk-8282@mail.ru')
        # # user_petya = User.objects.get(surname="Петя", email='andmarchu8@gmail.com')
        # group = Group.objects.create(name="Manager")
        # user_johndoe.groups.add(group)
        # user_johndoe.set_password('123qwe321')
        # user_johndoe.save()

        new_group = Group(name="Manager")
        new_group.save()

        course_content_type = ContentType.objects.get_for_model(Course)
        lesson_content_type = ContentType.objects.get_for_model(Lesson)

        add_permission_course = Permission.objects.get(codename="add_course", content_type=course_content_type)
        change_permission_course = Permission.objects.get(codename="change_course", content_type=course_content_type)
        delete_permission_course = Permission.objects.get(codename="delete_course", content_type=course_content_type)
        view_permission_course = Permission.objects.get(codename="view_course", content_type=course_content_type)

        add_permission_lesson = Permission.objects.get(codename="add_lesson",
                                                       content_type=lesson_content_type)
        change_permission_lesson = Permission.objects.get(codename="change_lesson",
                                                          content_type=lesson_content_type)
        delete_permission_lesson = Permission.objects.get(codename="delete_lesson",
                                                          content_type=lesson_content_type)
        view_permission_lesson = Permission.objects.get(codename="view_lesson",
                                                        content_type=lesson_content_type)

        new_group.permissions.add(add_permission_course, change_permission_course, delete_permission_course,
                                  view_permission_course, add_permission_lesson, change_permission_lesson,
                                  delete_permission_lesson, view_permission_lesson
                                  )
        new_group.save()

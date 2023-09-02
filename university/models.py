from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Course(models.Model):
    '''
    название курса,
    превью (картинка),
    описание.
    '''
    name_course = models.CharField(max_length=50, verbose_name='название курса')
    preview_course = models.ImageField(upload_to='Course/', verbose_name='изображение', **NULLABLE)
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f'{self.name_course}, {self.preview_course}, {self.description}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ('id',)


class Lesson(models.Model):
    '''
    название,
    описание,
    превью (картинка),
    ссылка на видео.
    '''
    name_lesson = models.CharField(max_length=50, verbose_name='название урока')
    description = models.TextField(verbose_name='описание')
    preview_lesson = models.ImageField(upload_to='Lesson/', verbose_name='изображение', **NULLABLE)
    link_video = models.URLField(max_length=150, **NULLABLE)

    def __str__(self):
        return f'{self.name_lesson}, {self.description}, {self.preview_lesson}, {self.link_video}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        ordering = ('id',)

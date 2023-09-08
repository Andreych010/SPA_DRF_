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
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lesson_key', verbose_name='курс', **NULLABLE)

    def __str__(self):
        return f'{self.name_lesson}, {self.description}, {self.preview_lesson}, {self.link_video}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        ordering = ('id',)


class Payments(models.Model):
    '''
    пользователь,
    дата оплаты,
    оплаченный курс или урок,
    сумма оплаты,
    способ оплаты: наличные или перевод на счет.
    '''
    PAYMENT_SPOT = 'spot'
    PAYMENT_CASHLESS = 'cashless'

    METH_PAYMENT = (
        (PAYMENT_SPOT, 'Наличный'),
        (PAYMENT_CASHLESS, 'Безналичный'),
    )

    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс', **NULLABLE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='урок', **NULLABLE)

    client = models.CharField(max_length=50, verbose_name='студент')
    date_payment = models.CharField(max_length=35, verbose_name='дата платежа')
    amount_payment = models.PositiveIntegerField(verbose_name='сумма оплаты')
    method_payment = models.CharField(max_length=35, choices=METH_PAYMENT,
                                      verbose_name='способ оплаты: наличные или перевод на счет')

    def __str__(self):
        return (f'{self.course if self.course else self.lesson} - {self.client}, '
                f'{self.date_payment}, {self.amount_payment}, {self.method_payment}')

    class Meta:
        verbose_name = 'Платёж'
        verbose_name_plural = 'Платежи'
        ordering = ('-date_payment',)

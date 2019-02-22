from django.db import models
from taggit.managers import TaggableManager


class Stuff(models.Model):
    # поясню позже
    FORWARDING_CHOICES = (
        ('not', 'не указано'),
        ('yes', 'да'),
        ('no', 'нет'),
    )
    # если verbose_name идет первым аргументом - название писать не нужно.
    # Этот аргумент первый по умолчанию (исключение ForeignKey и т.п.)
    title = models.CharField('Название лота', max_length=100)
    description = models.TextField('Описание лота', max_length=2000)

    # В эти два поля просятся auto_now_add и auto_now, и тогда нет смысла их выводить в админке
    date = models.DateField('Дата добавления лота')
    modifatedate = models.DateField('Дата изменения лота', blank=True, null=True)
    price = models.IntegerField('Цена', null=True)

    # Для чисел - числовые типы (IntegerField, FloatField, DecimalField и т.д.)
    lastprice = models.CharField('Предыдущая цена лота', max_length=10, blank=True)
    # blank=True и null=True одновременно - лишне. Для текстовых полей юзай blank=True
    lot_url = models.CharField('Ссылка на лот', max_length=200, blank=True, null=True)
    forwarding = models.CharField('Возможность пересыла', choices=FORWARDING_CHOICES, default='not', max_length=5)
    # без приставки "stuff_" не очевидно чья subcategory имеется в виду?
    stuff_subcategory = models.ForeignKey('SubCategory', on_delete=models.SET_NULL, verbose_name='Категория', blank=True, null=True)
    tags = TaggableManager()
    tags_temp = models.CharField('ТЕСТОВЫЕ теги', max_length=500, blank=True, null=True)
    city = models.ForeignKey('City', on_delete=models.SET_NULL,  verbose_name='Город', blank=True, null=True)
    city_temp = models.CharField('ТЕСТОВЫЕ города', max_length=30, blank=True, null=True)
    visible = models.BooleanField('Видимость', default=False, null=True)
    moderated = models.BooleanField('Прошел модерацию', default=False, null=True)
    ondelete = models.BooleanField('На удаление', default=False, null=True)

    # 1. здесь точно должен быть не BooleanField? 2. default=0, зачем кавычки?
    marked_spam = models.IntegerField('Помечено как Спам', default='0', null=True)
    marked_bad_category = models.IntegerField('Помечено как неверная категория', default='0', null=True)
    marked_soldout = models.IntegerField('Помечено как продано', default='0', null=True)
    marked_insult = models.IntegerField('Помечено как оскорбление', default='0', null=True)

    vk_page_id = models.IntegerField('ID страницы лота', blank=True, null=True)
    vk_album_id = models.IntegerField('ID альбома с лотом', blank=True, null=True)
    vk_owner_id = models.IntegerField('ID владельца группы', blank=True, null=True)
    vk_user_id = models.IntegerField('ID владельца лота', blank=True, null=True)
    vk_image_tumb_url = models.CharField('URL tumbnail изображения', max_length=500, blank=True, null=True)
    vk_image_url = models.CharField('URL изображения', max_length=500, blank=True, null=True)
    vk_image_host = models.CharField('URL хоста изображения', max_length=100, blank=True, null=True)
    # user = models.ForeignKey('',on_delete=models.CASCADE)

    class Meta:
        ordering = ["title"]
        verbose_name = "Лот"
        verbose_name_plural = "Лоты"

    def __str__(self):
        return self.title


class User(models.Model):
    # user = models.ForeignKey()
    telephone = models.CharField('Телефон', max_length=10)
    email = models.EmailField('Email', null=True)
    vk_user_id = models.IntegerField('ID пользователя VK', null=True)

    class Meta:
        ordering = ["pk"]
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Category(models.Model):
    title = models.CharField('Название категории', max_length=100)

    class Meta:
        ordering = ["title"]
        verbose_name = "Категория товара"
        verbose_name_plural = "Категории товаров"

    def __str__(self):
        return self.title


class SubCategory(models.Model):
    title = models.CharField('Название подкатегории', max_length=100)
    category = models.ForeignKey('Category', verbose_name='Категория товара', on_delete=models.PROTECT)

    class Meta:
        ordering = ["title"]
        verbose_name = "Подкатегория товара"
        verbose_name_plural = "Подкатегории товаров"

    def __str__(self):
        return self.title


class City(models.Model):
    title = models.CharField('Город', max_length=100)

    # Вариации будешь через запятую в одну строку вносить? =)
    # Это делается с помощью ArrayField
    variations = models.CharField('Вариации названия города', max_length=1000)

    class Meta:
        ordering = ["title"]
        verbose_name = "Город"
        verbose_name_plural = "Города"

    def __str__(self):
        return self.title

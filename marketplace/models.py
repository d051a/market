from django.db import models
from taggit.managers import TaggableManager
# Create your models here.


class Stuff(models.Model):
	FORWARDING_CHOICES = (
		('not', 'не указано'),
		('yes', 'да'),
		('no', 'нет'),
	)
	title = models.CharField(verbose_name='Название лота', max_length=100)
	description = models.TextField(verbose_name='Описание лота', max_length=2000)
	date = models.DateField('Дата добавления лота')
	modifatedate = models.DateField('Дата изменения лота', blank=True, null=True)
	price = models.CharField(verbose_name='Цена', max_length=10, blank=True)
	lastprice = models.CharField(verbose_name='Предыдущая цена лота', max_length=10, blank=True)
	lot_url = models.CharField('Ссылка на лот', max_length=200, blank=True, null=True)
	vk_page_id = models.IntegerField(verbose_name='ID страницы лота', blank=True, null=True)
	vk_album_id = models.IntegerField(verbose_name='ID альбома с лотом', blank=True, null=True)
	vk_owner_id = models.IntegerField(verbose_name='ID владельца группы', blank=True, null=True)
	vk_user_id = models.IntegerField(verbose_name='ID владельца лота', blank=True, null=True)
	forwarding = models.CharField(verbose_name='Возможность пересыла', choices=FORWARDING_CHOICES,
                                      default='not', max_length=5)
	stuff_subcategory = models.ForeignKey('SubCategory', on_delete=models.SET_NULL, verbose_name='Категория', blank=True, null=True)
	tags = TaggableManager()
	tags_temp = models.CharField(verbose_name='ТЕСТОВЫЕ теги', max_length=500, blank=True, null=True)
	city = models.ForeignKey('City', on_delete=models.SET_NULL,  verbose_name='Город', blank=True, null=True)
	city_temp = models.CharField(verbose_name='ТЕСТОВЫЕ города', max_length=30, blank=True, null=True)
	visible = models.BooleanField(verbose_name='Видимость', default=False, null=True)
	moderated = models.BooleanField(verbose_name='Прошел модерацию', default=False, null=True)
	ondelete = models.BooleanField(verbose_name='На удаление', default=False, null=True)
	marked_spam = models.IntegerField(verbose_name='Помечено как Спам', default='0', null=True)
	marked_bad_category = models.IntegerField(verbose_name='Помечено как неверная категория', default='0', null=True)
	marked_soldout = models.IntegerField(verbose_name='Помечено как продано', default='0', null=True)
	marked_insult = models.IntegerField(verbose_name='Помечено как оскорбление', default='0', null=True)

	vk_image_tumb_url = models.CharField(verbose_name='URL tumbnail изображения', max_length=500, blank=True, null=True)
	vk_image_url = models.CharField(verbose_name='URL изображения', max_length=500, blank=True, null=True)
	vk_image_host = models.CharField(verbose_name='URL хоста изображения', max_length=100, blank=True, null=True)
	#user = models.ForeignKey('',on_delete=models.CASCADE)

	class Meta:
		ordering = ["title"]
		verbose_name = "Лот"
		verbose_name_plural = "Лоты"

	def __str__(self):
		return self.title


class User(models.Model):
	#user = models.ForeignKey()
	telephone = models.CharField('Телефон', max_length=10)
	email = models.EmailField('Email', null=True)
	vk_user_id = models.IntegerField('ID пользователя VK', null=True)

	class Meta:
		ordering = ["pk"]
		verbose_name = "Пользователь"
		verbose_name_plural = "Пользователи"


class Category(models.Model):
	title = models.CharField(verbose_name='Название категории', max_length=100)

	class Meta:
		ordering = ["title"]
		verbose_name = "Категория товара"
		verbose_name_plural = "Категории товаров"

	def __str__(self):
		return self.title


class SubCategory(models.Model):
	title = models.CharField(verbose_name='Название подкатегории', max_length=100)
	category = models.ForeignKey('Category',verbose_name='Категория товара', on_delete=models.PROTECT)

	class Meta:
		ordering = ["title"]
		verbose_name = "Подкатегория товара"
		verbose_name_plural = "Подкатегории товаров"

	def __str__(self):
		return self.title


class City(models.Model):
	title = models.CharField(verbose_name='Город', max_length=100)
	variations = models.CharField(verbose_name='Вариации названия города', max_length=1000)

	class Meta:
		ordering = ["title"]
		verbose_name = "Город"
		verbose_name_plural = "Города"

	def __str__(self):
		return self.title

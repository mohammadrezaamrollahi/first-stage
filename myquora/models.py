from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    slug = models.SlugField(max_length=150, unique=True, allow_unicode=True, verbose_name=' نامک')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated = models.DateTimeField(auto_now=True, verbose_name='آخرین ویرایش')
    class Meta:
        verbose_name = 'دسته‌بندی'
        verbose_name_plural = 'دسته‌بندی‌ها'


    def __str__(self):
        return self.title

class Question(models.Model):
    PUBLISH_STATUS = (
        ('draft', 'پیش‌نویس'),
        ('publish', 'انتشار‌یافته')
    ) 
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نویسنده', related_name='question')
    question_title = models.CharField(max_length=200, verbose_name = "عنوان سوال")
    question_text = models.TextField(max_length=3000, verbose_name = "متن سوال")
    slug = models.SlugField(unique = True , verbose_name = "نامك")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='دسته‌بندی', related_name='question')
    status = models.CharField(max_length=15, verbose_name='وضعیت انتشار', choices=PUBLISH_STATUS, default='draft')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='آخرین ویرایش')
    number_like = models.IntegerField()
    number_report = models.IntegerField()
    class Meta:
        verbose_name = ("سوال")
        verbose_name_plural = ("سوال ها")
        
    def __str__(self):
        return self.question_title
'''
class tag (models.Model):
    Title = models.CharField(max_length=500 , unique = True , Verbose_name = "دسته بندي")
    slug = models.SlugField(unique = True , verbose_name = "نامك")
    '''

    





   

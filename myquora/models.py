from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.utils.text import slugify



class Tag(models.Model):
    tag_name = models.CharField(max_length=15, verbose_name="برچسب ها")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    updated_time = models.DateTimeField(auto_now=True, verbose_name="تاریخ به روزرسانی")

    class Meta:
        db_table = "tags"
        verbose_name = "برچسب"  
        verbose_name_plural = "برچسب ها"
        ordering = ('created_time',)


    def __str__(self):
        return self.tag_name
        

class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    slug = models.SlugField(max_length=150, unique=True, allow_unicode=True, verbose_name=' نامک')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated = models.DateTimeField(auto_now=True, verbose_name='آخرین ویرایش')
    class Meta:
        verbose_name = 'دسته‌بندی'
        verbose_name_plural = 'دسته‌بندی‌ها'
        ordering = ('created',)

    def __str__(self):
        return self.title

class Question(models.Model):
    # PUBLISH_STATUS = (
    #     ('draft', 'پیش‌نویس'),
    #     ('publish', 'انتشار‌یافته')
    # ) 
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نویسنده', related_name='questions')
    question_title = models.CharField(max_length=200, verbose_name = "عنوان سوال")
    # question_text = models.TextField(max_length=3000, verbose_name = "متن سوال")
    question_text = RichTextField(blank=True , null=True , verbose_name = "متن سوال")
    slug = models.SlugField(max_length=200 ,unique = True ,allow_unicode=True, verbose_name = "نامك")
    tag_question = models.ManyToManyField(Tag, verbose_name="برچسب")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='دسته‌بندی', related_name='questions')
    # status = models.CharField(max_length=15, verbose_name='وضعیت انتشار', choices=PUBLISH_STATUS, default='draft')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated = models.DateTimeField(auto_now=True, verbose_name='آخرین ویرایش')
    #number_like = models.IntegerField()
    #number_report = models.IntegerField()
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.question_title, allow_unicode=True)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("questions:question_detail", kwargs={"slug": self.slug})

    def get_user_full_name(self):
        return self.author.get_full_name()
    get_user_full_name.short_descriptin = "پرسشگر"

    class Meta:
        verbose_name = "سوال"
        verbose_name_plural = "سوال ها"
        ordering = ('created',)
        
    def __str__(self):
        return self.question_title

class Answer(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE ,verbose_name='سوال' ,  related_name='answers')
    slug = models.SlugField(max_length=150, unique=True, allow_unicode=True, verbose_name=' نامک')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated = models.DateTimeField(auto_now=True, verbose_name='آخرین ویرایش')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نویسنده', related_name='answers')
    #votes = models.IntegerField(default=0)
    content = RichTextField(verbose_name = "متن جواب")
    class Meta:
        verbose_name = ("جواب")
        verbose_name_plural = ("جواب ها")
        ordering = ('created',)
        
    def __str__(self):
        return self.content
    def get_user_full_name(self):
        return self.author.get_full_name()
    get_user_full_name.short_descriptin = "جواب دهنده"



    
    





   

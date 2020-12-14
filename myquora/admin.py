from django.contrib import admin
from myquora.models import Question , Category , Tag


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ["question_title", "created", "updated"]
    prepopulated_fields = {"slug": ("question_title",)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "created", "updated"]
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["tag_name", "created_time", "updated_time"]
    



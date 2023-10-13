from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.Category)

class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]
@admin.register(models.Mcqs)
class McqsAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title'
    ]
class AnserInlineModel(admin.TabularInline):
    model= models.Answer
    fields = [
        'answer_text',
        'is_right' 
    ]

@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'mcq'
    ]
    list_display = [
        'title',
        'mcq',
        'date_updated'
    ]
    inlines = [
        AnserInlineModel,
    ]

@admin.register(models.Answer)

class AnswerAdmin(admin.ModelAdmin):
    list_display = [
        'answer_text',
        'is_right',
        'question'
    ]
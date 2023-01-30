from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope



class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        tag = 0
        for form in self.forms:
            article = form.cleaned_data

            if article.get('is_main'):
                tag += 1
        if tag == 0:
            raise ValidationError('Укажите основной раздел')
        elif tag > 1:
            raise ValidationError('Основным может быть только один раздел')
        return super().clean()



class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 1
    formset = ScopeInlineFormset



@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'published_at', 'image']
    list_filter = ['title']
    inlines = [ScopeInline]



@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']



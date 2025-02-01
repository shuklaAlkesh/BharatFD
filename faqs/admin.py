# faqs/admin.py

from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import FAQ


class FAQAdminForm(forms.ModelForm):
    # Override specific fields to use the CKEditor widget
    answer = forms.CharField(widget=CKEditorWidget())
    answer_hi = forms.CharField(widget=CKEditorWidget(), required=False)
    answer_bn = forms.CharField(widget=CKEditorWidget(), required=False)

    class Meta:
        model = FAQ
        fields = '__all__'


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    form = FAQAdminForm

    # Example: Group fields in sets
    fieldsets = (
        ("English Content", {
            "fields": ("question", "answer")
        }),
        ("Hindi Content", {
            "fields": ("question_hi", "answer_hi")
        }),
        ("Bengali Content", {
            "fields": ("question_bn", "answer_bn")
        }),
        ("Metadata", {
            "fields": ("created_at", "updated_at"),
        }),
    )

    readonly_fields = ("created_at", "updated_at")

    list_display = ('question', 'created_at', 'updated_at')
    search_fields = ('question', 'question_hi', 'question_bn')

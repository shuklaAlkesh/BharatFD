from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator


class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()

    question_hi = models.TextField(null=True, blank=True)
    answer_hi = RichTextField(null=True, blank=True)
    question_bn = models.TextField(null=True, blank=True)
    answer_bn = RichTextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        """
        Override save to auto-generate translations if fields are empty.
        """
        translator = Translator()

        if not self.question_hi:
            translated = translator.translate(
                self.question, src='en', dest='hi')
            self.question_hi = translated.text
        if not self.answer_hi:
            translated = translator.translate(self.answer, src='en', dest='hi')
            self.answer_hi = translated.text

        if not self.question_bn:
            translated = translator.translate(
                self.question, src='en', dest='bn')
            self.question_bn = translated.text
        if not self.answer_bn:
            translated = translator.translate(self.answer, src='en', dest='bn')
            self.answer_bn = translated.text

        super().save(*args, **kwargs)

    def get_translated_question(self, lang='en'):
        """
        Return the question in the requested language, fallback to English.
        """
        if lang == 'hi' and self.question_hi:
            return self.question_hi
        elif lang == 'bn' and self.question_bn:
            return self.question_bn
        return self.question

    def get_translated_answer(self, lang='en'):
        """
        Return the answer in the requested language, fallback to English.
        """
        if lang == 'hi' and self.answer_hi:
            return self.answer_hi
        elif lang == 'bn' and self.answer_bn:
            return self.answer_bn
        return self.answer

    def __str__(self):
        return f"FAQ: {self.question[:50]}..."

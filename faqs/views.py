from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.cache import cache
from django.conf import settings

from .models import FAQ
from .serializers import FAQSerializer


@api_view(['GET', 'POST'])
def faq_list_create(request):
    """
    GET: List all FAQs in requested language (?lang=hi/bn/en).
    POST: Create a new FAQ with English question/answer, auto-translate to others.
    """
    if request.method == 'GET':
        lang = request.GET.get('lang', 'en')
        cache_key = f'faqs_{lang}'
        faqs_data = cache.get(cache_key)

        if not faqs_data:
            faqs_data = []
            for faq in FAQ.objects.all():
                faqs_data.append({
                    'id': faq.id,
                    'question': faq.get_translated_question(lang),
                    'answer': faq.get_translated_answer(lang),
                    'created_at': faq.created_at,
                    'updated_at': faq.updated_at
                })
            cache.set(cache_key, faqs_data, timeout=settings.CACHE_TTL)

        return Response(faqs_data)

    elif request.method == 'POST':
        serializer = FAQSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Invalidate cache so new data is reflected
            cache.delete_pattern('faqs_*')
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

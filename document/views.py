from django.shortcuts import render
from django.conf import settings

from .models import Document

# Create your views here.
def doc_list(product_type):
    docs = {}
    for i in settings.CONSTANTS['document_choices']:
        docs[i[0]] = Document.objects.filter(product_type=product_type, document_type=i[0])

    return docs

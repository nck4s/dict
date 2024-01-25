from django.shortcuts import render, get_object_or_404
from .models import Dictionary


def word_detail(request, word):
    word = get_object_or_404(Dictionary, word=word)
    return render(request, 'word_detail.html', {'word': word})
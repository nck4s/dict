from django.shortcuts import render, get_object_or_404
from .models import Dictionary


def main_page(request):
    return render(request, 'main_page.html')


def search_results(request):
    if request.method == 'GET':
        query = request.GET.get('q', '')
        results = Dictionary.objects.filter(word__icontains=query)
        context = {'results': results, 'query': query}
        return render(request, 'search_results.html', context)


def word_detail(request, word):
    word = get_object_or_404(Dictionary, word=word)
    return render(request, 'word_detail.html', {'word': word})
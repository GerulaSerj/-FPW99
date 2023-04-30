from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import re

words = []

def load(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        with open(fs.path(filename), 'r') as f:
            contents = f.read()
            global words
            words = re.findall(r'\b[a-zA-Z]+\b', contents)
        return HttpResponse(f"{len(words)} words loaded from {file.name}")
    return render(request, 'load.html')

def wordcount(request):
    if request.method == 'POST':
        word = request.POST.get('word')
        count = words.count(word)
        return HttpResponse(f"{word} occurs {count} times")
    return render(request, 'wordcount.html')

def clear_memory(request):
    global words
    words = []
    return HttpResponse("Memory cleared")
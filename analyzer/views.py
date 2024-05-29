from django.shortcuts import render
from .forms import UploadFileForm
import re
from collections import Counter


def index(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            content = file.read().decode('utf-8')

            word_count = len(re.findall(r'\b\w+\b', content))
            sentence_count = len(re.findall(r'[.!?]', content))
            word_frequencies = Counter(re.findall(r'\b\w+\b', content))

            return render(request, 'analyzer/result.html', {
                          'word_count': word_count,
                          'sentence_count': sentence_count,
                          'word_frequencies': word_frequencies,
                          })
    else:
        form = UploadFileForm()
    return render(request, 'analyzer/index.html', {'form': form})

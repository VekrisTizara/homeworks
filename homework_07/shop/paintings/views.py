from django.shortcuts import render

from .models import Painting


def index(request):
    all_paintings = Painting.objects.all()
    context = {
        'all_paintings': all_paintings
    }
    return render(request, 'index.html', context=context)

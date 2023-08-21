from django.shortcuts import render
from .models import *


def index(request):
    data_ex = Experience.objects.all()
    data_ed = Education.objects.all()
    return render(request, 'pf_app/index.html', {
        'data_ex': data_ex,
        'data_ed': data_ed
    })

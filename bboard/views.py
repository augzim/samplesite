from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Bb


def index(request):
    bbs = Bb.objects.all()
    context = {'bbs': bbs}
    return render(request, 'bboard/index.html', {'bbs': bbs})

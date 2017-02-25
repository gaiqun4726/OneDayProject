from django.shortcuts import render
from django.http import JsonResponse
from random import random
# from modules


# Create your views here.

def show3DScatters(request):
    return render(request, 'study/3DScatters.html')


def showAjaxhtml(request):
    return render(request, 'study/testajax.html')


def ajax_list(request):
    a = range(100)
    return JsonResponse(a, safe=False)


def ajax_dict(request):
    name_dict = {'twz': 'Love python and Django', 'zqxt': 'I am teaching Django'}
    return JsonResponse(name_dict)


def getLocation(request):
    return render(request, 'study/location.html')


def getLocation2(request):
    return render(request, 'study/location2.html')


def generateRandom(request):
    x = random()
    y = random()
    return JsonResponse([x, y], safe=False)

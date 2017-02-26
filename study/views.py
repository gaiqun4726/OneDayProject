from django.shortcuts import render
from django.http import JsonResponse
from random import random
import Queue
from .modules.collector import *
from .modules.preprocessor import *
from .modules.loader import *
from .modules.locator import *


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


receiverThread = Receiver('receiver')
collectorThread = Collector('collector')
preprocessorThread = Preprocessor('preprocessor')

receiverThread.start()
collectorThread.start()
preprocessorThread.start()

spectrumLoader = SpectrumLoader()
spectrumLoader.loadSpectrum()

locationDictLoader = LocationDictLoader()
locationDictLoader.loadLoactionDict()
locator = Locator()


def getLocation(request):
    return render(request, 'study/location.html')


def getLocation2(request):

    return render(request, 'study/location2.html')


def generateRandom(request):
    x = 39
    y = 25
    return JsonResponse([x, y], safe=False)


def getCord(request):
    res = locator.getLoacatingMessage()
    print res
    return JsonResponse(res, safe=False)

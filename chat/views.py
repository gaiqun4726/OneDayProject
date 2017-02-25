from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'chat/comment.html')


def test(request, dic):
    print dic
    return render(request, 'chat/test.html')

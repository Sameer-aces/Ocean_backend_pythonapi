from django.shortcuts import HttpResponse

# Create your views here.
def start(request):
    return HttpResponse('<h1> Server Started </h1>')
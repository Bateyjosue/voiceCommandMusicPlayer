from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    if request.method == 'GET':
      status = request.GET.get('task')
      print(status)
    return render(request, 'player/index.html')
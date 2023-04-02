from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt



def list(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@csrf_exempt 
def insert(request):
    if request.method == 'POST':
     return HttpResponse("Hello, insert.")

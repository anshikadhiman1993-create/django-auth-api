from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello! Django is working on Azure ✅")

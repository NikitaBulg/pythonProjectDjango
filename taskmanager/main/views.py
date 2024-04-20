from django.http import HttpResponse
from django.conf import settings
settings.configure()

def index(request):
    return HttpResponse("Hello, world. You're at the")

from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("hello world")
    
def requete_nominatim(request):
    pass

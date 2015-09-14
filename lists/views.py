from django.http import HttpResponse

# Create your views here.
def home_page(request):
    return HttpResponse('<html><title>To-Do lists</title><body>Nama : Agnes Agustinamora<br>NPM : 1206239421</body></html>')
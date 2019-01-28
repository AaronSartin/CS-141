from django.shortcuts import render

# Create your views here.
def index(request):
    #template = loader.get_template('home/index.html')
    context = {}
    return render(request, 'home/index.html', context)
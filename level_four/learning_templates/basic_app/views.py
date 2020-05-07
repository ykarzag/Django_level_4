from django.shortcuts import render

# Create your views here.
def index(request):
    print('in index')
    return render(request,'basic_app/index.html')

def other(request):
    return render(request,'basic_app/other.html')

def relative(request):
    print('in relative')
    return render(request,'basic_app/relative_url_templates.html')

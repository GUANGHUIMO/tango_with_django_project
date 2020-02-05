from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #return HttpResponse("Rango says hey there partner! <a href='/rango/about/'>About</a>")
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context=context_dict)
def about(request):
    # Spoiler: you don't need to pass a context dictionary here.
    return render(request, 'rango/about.html')#不需要context，因为是用来传string的。




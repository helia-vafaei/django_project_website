from django.http.response import HttpResponse
from django.shortcuts import render
from .models import book
# Create your views here.
        
def modernform(request):
    if request.method == 'GET' :
        return render(request , 'modernform.html')
    #if request.method == 'POST' :    

def show(request):
    genre = request.POST['genre']
    result = book.objects.filter(genre=genre)
    context = {"books" : result}
    return render(request, 'show.html', context=context)

def show2(request):
    if request.method == 'GET' :
        return render(request , 'show2.html')
    if request.method == 'POST' :       
        name=request.POST['name']
        writer=request.POST['writer']
        genre=request.POST['genre']
        summery = request.POST['summery']
        result = book.objects.create(name=name ,writer=writer,summery=summery,genre=genre)
        context = {"books" : result}
        return render(request, 'show2.html', context=context)




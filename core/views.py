from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse('<h1 style="text-align:center;">Hello {}</h1></b><h2 style="text-align:center;color:red;">Idade = {}</h2>'.format(nome,idade))

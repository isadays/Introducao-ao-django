from django.shortcuts import render, HttpResponse


# Create your views here.
def hello(request, nome, idade):
    return HttpResponse('<h1>Meu primeiro Projeto Django. Olá {}, de {} anos !</h1>'.format(nome, idade))


def soma(request, num1, num2):
        return HttpResponse('A soma entre {} e {} é igual a {}'.format(num1, num2, num1 + num2))


def divisao(request,num1,num2):
        return HttpResponse('A divisao entre {} e {} é igual a {}'.format(num1, num2, num1 / num2))


def subtracao(request,num1,num2):
       return HttpResponse('A subtracao entre {} e {} é igual a {}'.format(num1, num2, num1 - num2))


def multiplicacao(request,num1,num2):
    return HttpResponse('A multiplicacao entre {} e {} é igual a {}'.format(num1, num2, num1 * num2))

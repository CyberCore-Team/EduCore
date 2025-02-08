from django.shortcuts import render
from django.http import HttpResponse

def index(request): #index замість manepage ,ага я трішки ідіот ,переназивати мені лінь , сам зробиш якщо хоч
    return render(request, 'mainpage/index.html')  #показує головну сторінку через html(терба би переробити назву програми з mainpage на щось типу main, але мені лінь

def loginpage(request):
    return render(request, 'mainpage/loginpage.html') #показує сторінку авторізації через html(login)

def registpage(request):
    return render(request, 'mainpage/registpage.html') #показує сторінку регістрації через html(regist)

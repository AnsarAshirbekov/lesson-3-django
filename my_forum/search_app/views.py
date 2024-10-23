from django.shortcuts import render

from django.http import HttpResponse

def search_view(request):
    return HttpResponse("""
        <h1> Поиск темы </h1>
        <p> Страница поиска тем </p>
        <a href="/"> Главная </a><br>
        <a href="/users/"> Профиль пользователя </a><br> 
""")

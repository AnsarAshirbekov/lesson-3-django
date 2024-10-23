from django.shortcuts import render

from django.http import HttpResponse

def users_view(request):
    return HttpResponse("""
        <h1> Твой профиль </h1>
        <p> Страница профиля пользователя </p>
        <a href="/"> Главная </a><br>
        <a href="/search/"> Поиск темы </a><br> 
""")

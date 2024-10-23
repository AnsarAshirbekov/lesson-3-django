from django.shortcuts import render

from django.http import HttpResponse

def forum_view(request):
    return HttpResponse("""
        <h1> Форум электриков </h1>
        <p> Главная страница форума </p>
        <a href="/users/"> Профиль пользователя </a><br>
        <a href="/search/"> Поиск темы </a><br> 
""")

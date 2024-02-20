from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    http = '''
    <h1>Добро пожаловать в джанго</h1>
    <p>Я сделал этот сайт с помощью джанго :) Вот небольшая информация:</p>
    <ul>
        <li>Была использована версия Джанго 5.0.2</li>
        <li>Я сделал это менее чем за 30 минут</li>
        <li>Я делаю это в час ночи :)</li>
    </ul>
    <p>Очень хороший сайт :)</p>
    '''
    return HttpResponse(http)

def about(request):
    http = '''
    <h1>Немного обо мне</h1>
    <p>Вставьте небольшую информацию обо мне</p>
    <h2>Что-то</h2>
    <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Blanditiis amet facere, reiciendis placeat maxime rem.</p>
    <ul>
        <li>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Itaque, recusandae.</li>
        <li>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Officia nostrum eaque veniam.</li>
        <li>Lorem ipsum dolor sit amet consectetur adipisicing elit.</li>
    </ul>
    <h2>Что-то</h2>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Iste sapiente illo omnis a. Impedit porro, asperiores quas incidunt laborum voluptates cum odio maiores officia ex quidem id mollitia itaque voluptate dolore numquam facere autem deserunt doloribus, aperiam libero provident dicta sapiente. Harum, sequi neque aperiam earum culpa laboriosam ratione sit?</p>
    <h1>Все :)</h1>
    '''
    return HttpResponse(http)
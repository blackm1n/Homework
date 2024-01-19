from flask import Flask
from flask import render_template
import lorem
import random

app = Flask('shop')


items = {'jackets': [{'image': '../static/files/jacket.png', 'name': 'Куртка №1', 'description': lorem.sentence()},
                     {'image': '../static/files/jacket.png', 'name': 'Куртка №2', 'description': lorem.sentence()},
                     {'image': '../static/files/jacket.png', 'name': 'Куртка №3', 'description': lorem.sentence()}],
         'shoes': [{'image': '../static/files/shoes.png', 'name': 'Обувь №1', 'description': lorem.sentence()},
                   {'image': '../static/files/shoes.png', 'name': 'Обувь №2', 'description': lorem.sentence()},
                   {'image': '../static/files/shoes.png', 'name': 'Обувь №3', 'description': lorem.sentence()}]}

@app.route('/')
def clothes():
    context = {'categories': [{'name': 'Куртка', 'item': random.choice(items.get('jackets'))},
                              {'name': 'Обувь', 'item': random.choice(items.get('shoes'))}]}
    return render_template('main.html', **context)


@app.route('/jackets/')
def jackets():
    context = {'name': 'Куртки', 'items': items.get('jackets')}
    return render_template('category.html', **context)


@app.route('/shoes/')
def shoes():
    context = {'name': 'Обувь', 'items': items.get('shoes')}
    return render_template('category.html', **context)


if __name__ == '__main__':
    app.run()

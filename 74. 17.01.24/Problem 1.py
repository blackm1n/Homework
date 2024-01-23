from flask import Flask, render_template, redirect, url_for, request, make_response

app = Flask('login')


@app.get('/')
def login_get():
    if request.cookies.get('username'):
        return redirect(url_for('hello_get'))
    return render_template('login.html')


@app.post('/')
def login_post():
    response = make_response(redirect(url_for('hello_get')))
    response.set_cookie('username', request.form.get('username'))
    response.set_cookie('email', request.form.get('email'))
    return response


@app.get('/hello/')
def hello_get():
    context = {'username': request.cookies.get('username')}
    return render_template('hello.html', **context)


@app.post('/hello/')
def hello_post():
    response = make_response(redirect(url_for('login_get')))
    response.delete_cookie('username')
    response.delete_cookie('email')
    return response


if __name__ == '__main__':
    app.run()

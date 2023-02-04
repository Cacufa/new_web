from flask import Flask, request, make_response, redirect, render_template
from flask_bootstrap import Bootstrap


app =  Flask(__name__)
Bootstrap = Bootstrap(app) # creates an instance to work with bootstrap

todos = ['Compras', 'Ventas', 'Estados'] # iterable list for testing

@app.errorhandler(404) # error handler 404
def not_found(error):
    return render_template('404.html', error=error)


@app.route("/")
def index():
    user_ip = request.remote_addr
    
    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip', user_ip) 
    
    return response

@app.route("/hello")
def hello():
    user_ip = request.cookies.get('user_ip')
    context = {
        'user_ip': user_ip,
        'todos': todos
    }
    return render_template('hello.html', **context)

@app.route('/contenido')
def contenido():
    return render_template('contenido.html')
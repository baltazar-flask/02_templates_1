from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)

# Control structures - if / elif / else
@app.route('/if_else')
def if_else():
    #name = None
    name = "Baltazar"
    return render_template('if_else.html',name=name)
# http://localhost:5000/if-else - Pozdrav, neznanče!

# Control structures - for
@app.route('/for')
def for_loop():
    oss = ['Windows 7','Windows 10','Windows 11']
    return render_template('for.html',oss=oss)
# http://localhost:5000/for/
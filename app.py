from flask import Flask
app = Flask(__name__)
from flask import render_template


@app.route('/')
def hello(name='Kam'):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run()
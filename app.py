from flask import Flask, request,  render_template
app = Flask(__name__)


@app.route('/')
def hello(name=None):
    form_name = request.form['name']
    return render_template('hello.html', name=name)


@app.route('/handle_name_submit', methods=['POST'])
def handle_data():
    form_name = request.form['name']
    return render_template('hello.html', name=form_name)


@app.route('/handle_madlibs_data', methods=['POST'])
def handle_data():
    form_verb = request.form['verb']
    form_adverb = request.form['adverb']
    form_adjective = request.form['adjective']
    form_noun = request.form['noun']

    return render_template('hello.html', name=form_verb)


if __name__ == '__main__':
    app.run()
from flask import Flask, request,  render_template
app = Flask(__name__)


@app.route('/')
def hello(name=None):
    # form_name = request.form['name']
    return render_template('hello.html')


@app.route('/handle_name_submit', methods=['POST'])
def handle_name_submit():
    form_name = request.form['name']
    return render_template('hello.html', name=form_name)


@app.route('/handle_madlibs_data', methods=['POST'])
def handle_madlibs_data():
    form_adjective1 = request.form['adjective1']
    form_adjective2 = request.form['adjective2']
    form_noun1 = request.form['noun1']
    form_noun2 = request.form['noun2']
    form_plunoun1 = request.form['plunoun1']
    form_game = request.form['game']
    form_plunoun2 = request.form['plunoun2']
    form_verbing1 = request.form['verbing1']
    form_verbing2 = request.form['verbing2']
    form_plunoun3 = request.form['plunoun3']
    form_verbing3 = request.form['verbing3']
    form_noun4 = request.form['noun4']
    form_plant = request.form['plant']
    form_bodypart = request.form['bodypart']
    form_place = request.form['place']
    form_verbing4 = request.form['verbing4']
    form_adjective3 = request.form['adjective3']
    form_number = request.form['number']
    form_plunoun4 = request.form['plunoun4']

    return render_template('madLibs1.html', verb=form_verb, adverb=form_adverb, adjective=form_adjective, noun=form_noun)


if __name__ == '__main__':
    app.run()

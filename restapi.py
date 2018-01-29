from flask import Flask, render_template

from risk_monte_carlo import run_simulations

app = Flask(__name__)


@app.route('/')
def show_options():
    return render_template('index.html')

@app.route('/<int:i>')
@app.route('/<int:i>/<int:j>')
def show_thing(i,j=None):
    return "Howdy"


@app.route('/<int:sim_num>/<int:attack_num>/<int:defense_num>')
def show_convoluted_url(sim_num=10, attack_num=5, defense_num=2):
    results = run_simulations(sim_num, attack_num, defense_num)
    return render_template('convoluted.html',
                           attack_num=attack_num,
                           defense_num=defense_num,
                           sim_num=sim_num,
                           results=results)


if __name__ == '__main__':
    app.run(debug=True)

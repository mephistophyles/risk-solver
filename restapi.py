import base64
import io

from flask import Flask, render_template, request

from risk_monte_carlo import graph_results, run_simulations

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def show_options():
    if request.method == "POST":
        if request.form.getlist('results_text'):
            text_output = True
        else:
            text_output = False
        if request.form.getlist('house_rules'):
            house_rules_check = True
        else:
            house_rules_check = False
        results = run_simulations(int(request.form['simulations']),
                                  int(request.form['attacking_armies']),
                                  int(request.form['defending_armies']),
                                  house_rules=house_rules_check)
        plt = graph_results(results, type="scatter")
        fig_file = io.BytesIO()
        plt.savefig(fig_file, format='png')
        fig_file.seek(0)
        fig = base64.b64encode(fig_file.getvalue()).decode()
        return render_template('index.html', results=results, fig=fig, results_text=text_output)
    else:
        return render_template('index.html')

@app.route('/<int:i>')
@app.route('/<int:i>/<int:j>')
def show_thing(i,j=None):
    return render_template('incorrect_url.html')


@app.route('/<int:sim_num>/<int:attack_num>/<int:defense_num>', methods=['POST', 'GET'])
def show_convoluted_url(sim_num=10, attack_num=5, defense_num=2):
    results = run_simulations(sim_num, attack_num, defense_num)
    return render_template('convoluted.html',
                           attack_num=attack_num,
                           defense_num=defense_num,
                           sim_num=sim_num,
                           results=results)


if __name__ == '__main__':
    app.run(debug=True)

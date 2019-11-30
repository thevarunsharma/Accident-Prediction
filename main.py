from flask import Flask, request, render_template
from naive_bayes import Bayesian_Probability, NaiveBayes
from pickle import load

with open("./cleaned/Probs.dat", "rb") as fh:
    # dict containng bayesian probabilities
    Probs = load(fh)

with open("./cleaned/state-map.dat", "rb") as fh:
    # mapping of state name to its other alternative names
    state_map = load(fh)

# naive bayes predictor
predictor = NaiveBayes(Probs, state_map)

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def main():
    if request.method == 'POST':
        data = request.form
        state = data['state']
        type_of_road = data['type_of_road']
        location = data['location']
        license = data['license']
        vehicle = data['vehicle']
        drunk = True if data['drunk'] == 'Drunk' else False
        junction = data['junction'].lower() if data['is_junction'] == 'y' else None
        perc = "%.4f%%"%predictor.get_probability(state, type_of_road, location, license, vehicle, drunk, junction)
        return render_template('main.html', after_srch=True, perc=perc)
    return render_template('main.html', after_srch=False)

app.config["TEMPLATES_AUTO_RELOAD"] = True
app.run(debug=True)

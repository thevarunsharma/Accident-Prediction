import sys
from flask import Flask, request, render_template, redirect, url_for
from Accident_Prediction.naive_bayes import Bayesian_Probability, NaiveBayes
from pickle import load

sys.modules['__main__'].Bayesian_Probability = Bayesian_Probability

with open("./Accident_Prediction/cleaned/Probs.dat", "rb") as fh:
    # dict containng bayesian probabilities
    Probs = load(fh)

with open("./Accident_Prediction/cleaned/state-map.dat", "rb") as fh:
    # mapping of state name to its other alternative names
    state_map = load(fh)

# naive bayes predictor
predictor = NaiveBayes(Probs, state_map)
app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        return redirect(url_for('result'), code=307)
    return render_template('home.html')

@app.route('/result', methods=['POST'])
def result():
    data = request.form
    if not data:
        return redirect(url_for('home'))
    state = data['state']
    type_of_road = data['type_of_road']
    type_of_weather = data['type_of_weather']
    location = data['location']
    license = data['license']
    vehicle = data['vehicle']
    drunk = True if data['drunk'] == 'Drunk' else False
    junction = data['junction']
    perc = "%.4f%%"%predictor.get_probability(state, type_of_road, type_of_weather, location, license, vehicle, drunk, junction)
    return render_template('result.html', perc=perc, data=data)

app.config["TEMPLATES_AUTO_RELOAD"] = True
if __name__ == '__main__':
    app.run(debug=True)

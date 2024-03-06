from flask import Flask, render_template, request
import src.utils as utils
from src.prediction_model import identify_waste_type

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/start')
def insert():
    utils.open_waste_slot()

    return render_template('insert.html')


@app.route('/waste/pick-type', methods=['POST'])
def pick_type():
    utils.close_waste_slot()
    waste_url = request.form['waste_url']
    res, exc = identify_waste_type(waste_url)
    if exc != "":
        return render_template('error_handler.html', error=exc)
    else:
        check_bottle = "" if res.get("bottle") < 0.5 else "checked=\"checked\""
        check_cutlery = "" if res.get("cutlery") < 0.5 else "checked=\"checked\""
        check_glass = "" if res.get("glass") < 0.5 else "checked=\"checked\""

        return render_template('type.html', 
                               check_bottle=check_bottle, 
                               check_cutlery=check_cutlery, 
                               check_glass=check_glass,
                               error=exc)


@app.route('/confirmation', methods=['POST'])
def confirmation():
    waste_type = request.form['type']

    utils.process_waste(waste_type)
    return render_template('confirmation.html')


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request
# from sklearn.externals import joblib
import joblib

app = Flask(__name__)


@app.route('/')
def index():
    prediction = prediction = preprocessDataAndPredict("I am sad")
    print(prediction)

    return render_template('index.html')


@app.route('/predict/', methods=['GET', 'POST'])
def predict():
    if request.method == "POST":

        # get form data
        txt = request.form.get('txt')

        # call Predictmood and pass inputs
        try:
            prediction = preprocessDataAndPredict(txt)
            # pass prediction to template
            return render_template('predict.html', prediction=prediction)

        except ValueError:
            return "Please Enter valid values"

        pass
    pass


def preprocessDataAndPredict(txt):
    # open file
    # file = open("model/mode.pkl","rb")

    # load trained model
    trained_model = joblib.load("model/mode.pkl")

    # predict
    prediction = trained_model.predict([txt])
    print(prediction)
    return prediction

    pass


if __name__ == '__main__':
    app.run(debug=True)

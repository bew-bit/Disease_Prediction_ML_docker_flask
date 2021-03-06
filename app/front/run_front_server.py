import json

from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from requests.exceptions import ConnectionError
from wtforms import IntegerField, SelectField, StringField
from wtforms.validators import DataRequired

import urllib.request
import json

class ClientDataForm(FlaskForm):
    age = StringField('age', validators=[DataRequired()])
    gender = StringField('gender', validators=[DataRequired()])
    height = StringField('height', validators=[DataRequired()])
    weight = StringField('weight', validators=[DataRequired()])
    ap_hi = StringField('ap_hi', validators=[DataRequired()])
    ap_lo = StringField('ap_lo', validators=[DataRequired()])
    cholesterol = StringField('cholesterol', validators=[DataRequired()])
    gluc = StringField('gluc', validators=[DataRequired()])
    smoke = StringField('smoke', validators=[DataRequired()])
    alco = StringField('alco', validators=[DataRequired()])
    active = StringField('active', validators=[DataRequired()])


app = Flask(__name__)
app.config.update(
    CSRF_ENABLED=True,
    SECRET_KEY='you-will-never-guess',
)

def get_prediction(age, gender, height, weight, ap_hi, ap_lo, cholesterol, gluc, smoke, alco, active):
    body = {'age': age,
            'gender': gender,
            'height': height,
            'weight': weight,
            'ap_hi': ap_hi,
            'ap_lo': ap_lo,
            'cholesterol': cholesterol,
            'gluc': gluc,
            'smoke': smoke,
            'alco': alco,
            'active': active}

    myurl = "http://0.0.0.0:8180/predict"
    req = urllib.request.Request(myurl)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    jsondata = json.dumps(body)
    jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
    req.add_header('Content-Length', len(jsondataasbytes))
    #print (jsondataasbytes)
    response = urllib.request.urlopen(req, jsondataasbytes)
    return json.loads(response.read())['predictions']

@app.route("/")
def index():
    return render_template('index.html')


@app.route('/predicted/<response>')
def predicted(response):
    response = json.loads(response)
    print(response)
    return render_template('predicted.html', response=response)


@app.route('/predict_form', methods=['GET', 'POST'])
def predict_form():
    form = ClientDataForm()
    data = dict()
    if request.method == 'POST':
        data['age'] = request.form.get('age')
        data['gender'] = request.form.get('gender')
        data['height'] = request.form.get('height')
        data['weight'] = request.form.get('weight')
        data['ap_hi'] = request.form.get('ap_hi')
        data['ap_lo'] = request.form.get('ap_lo')
        data['cholesterol'] = request.form.get('cholesterol')
        data['gluc'] = request.form.get('gluc')
        data['smoke'] = request.form.get('smoke')
        data['alco'] = request.form.get('alco')
        data['active'] = request.form.get('active')


        try:
            response = str(get_prediction(data['age'],
                                          data['gender'],
                                          data['height'],
                                          data['weight'],
                                          data['ap_hi'],
                                          data['ap_lo'],
                                          data['cholesterol'],
                                          data['gluc'],
                                          data['smoke'],
                                          data['alco'],
                                          data['active']))
            print(response)
        except ConnectionError:
            response = json.dumps({"error": "ConnectionError"})
        return redirect(url_for('predicted', response=response))
    return render_template('form.html', form=form)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8181, debug=True)
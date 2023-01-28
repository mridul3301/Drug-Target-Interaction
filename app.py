import numpy as np
from flask import Flask, request, jsonify, render_template
from sklearn.linear_model import _base
from DeepPurpose import utils
from DeepPurpose import  DTI as models
import pickle

app = Flask(__name__)
#model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    drug_encoding, target_encoding = 'Transformer', 'CNN'

    features = [[x] for x in request.form.values()]

    X_drug = features[0]
    X_target = features[1]
    y = [1]

    X_pred = utils.data_process(X_drug, X_target, y,
                                drug_encoding, target_encoding, 
                                split_method='no_split')

    dti_model = models.model_pretrained(path_dir = 'DTI_Model')
    y_pred = dti_model.predict(X_pred)

    #final_features = [np.array(int_features)]
    #prediction = model.predict(final_features)

    output = str(y_pred)

    return render_template('index.html', prediction_text='Binding Affinity = {}'.format(output))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)
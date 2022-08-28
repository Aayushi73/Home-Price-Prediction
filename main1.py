import pickle
import numpy as np
from flask import Flask,render_template,request

app = Flask(__name__)
model = pickle.load(open('model1.pkl','rb'))

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict',methods=['GET','POST'])
def predict():
    try:
        def pred(predict_list):
            to_predict = np.array(predict_list).reshape(1, 12)
            result = model.predict(to_predict)
            return result
    
        if request.method == 'POST':
            predict_list = request.form.to_dict()
            predict_list = list(predict_list.values())
            predict_list = list(map(int, predict_list))
            result = pred(predict_list)
            return render_template('index.html' , prediction_text = int(result))

    except:
        return render_template('index.html' , prediction_text = "Please enter valid data")

if __name__ == '__main__':
    app.run(debug=True)
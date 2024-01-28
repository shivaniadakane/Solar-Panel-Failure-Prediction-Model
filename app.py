


from flask import Flask, render_template, request
import pandas as pd
import pickle
import joblib
import numpy as np

model = pickle.load(open('rf_clf_par.pkl','rb'))
Winsorizer= joblib.load('Winsorizer')
minmax = joblib.load('minmax')


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')



@app.route('/success', methods = ['POST'])
def success():
    if request.method == 'POST' :
        f = request.files['file']
        new_df = pd.read_csv(f)
        newdata = pd.DataFrame(Winsorizer.transform(new_df[['Ipv', 'Vpv', 'Vdc', 'ia', 'ib', 'ic','va', 'vb', 'vc', 'Iabc', 'If', 'Vabc', 'Vf']]))
        newminmax = pd.DataFrame(minmax.transform(newdata), columns = new_df.select_dtypes(exclude = ['object']).columns)
        predictions = pd.DataFrame(model.predict(newminmax),columns = ['label'])
        final = pd.concat([predictions, new_df], axis = 1)
        return render_template("new.html", Y = final.to_html(justify = 'center'))


def ValuePredictor(to_predict_list):
	to_predict = np.array(to_predict_list).reshape(1, 13)
	loaded_model = pickle.load(open('rf_clf_par.pkl','rb'))
	result = loaded_model.predict(to_predict)
	return result[0]

@app.route('/result', methods = ['POST'])
def result():
	if request.method == 'POST':
		to_predict_list = request.form.to_dict()
		to_predict_list = list(to_predict_list.values())
		to_predict_list = list(map(float, to_predict_list))
		result = ValuePredictor(to_predict_list)	
		if result== 1:
			prediction ='Solar Panel Is Not Faulty'
		else:
			prediction ='Solar Panel Is Faulty'		
		return render_template("index.html", prediction = prediction)


if __name__=='__main__':
    app.run(debug = True)



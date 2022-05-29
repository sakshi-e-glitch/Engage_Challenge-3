# from unittest.result import failfast
# from crypt import methods
import html
# from flask import Flask, render_template, url_for, Response, request, redirect, *
from flask import *
import openpyxl
# from flask_sqlalchemy import SQLAlchemy

# Importing pandas library
import pandas as pd
# Importing sklearn library. This is a very powerfull library for machine learning. Scikit-learn is probably the most useful library for machine learning in Python. The sklearn library contains a lot of efficient tools for machine learning and statistical modeling including classification, regression, clustering and dimensionality reduction.
from sklearn import preprocessing
# Importing Knn Classifier from sklearn library.
from sklearn.neighbors import KNeighborsClassifier
# Importing numpy to do stuffs related to arrays
import numpy as np
# import PySimpleGUI as sg
from sklearn import metrics

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# test = SQLAlchemy(app)

# class Result(test.Model):
#     ans = test.Column(test.String(200))
#     def __repr__(self) -> str:
#         return f"{self.ans}"


# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

# if __name__ == "__main__":
#     app.run(debug=True)

# @app.route("/")
# def hello_world():
#     return "Hello World"

# @app.route("/index")
# def main():
#     return render_template('index.html')

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/recommender")
def index():
    return render_template('recommender.html')

@app.route("/news")
def news():
    return render_template('news.html')

@app.route("/plants")
def plants():
    return render_template('plants.html')    

@app.route("/recommenderafter" , methods=["GET","POST"])
def crop_prediction():
    if request.method == "POST":
        nitrogen = request.form.get("n")
      # getting input with name = lname in HTML form
        phosphorus = request.form.get("ph")
        potassium = request.form.get("k")
        temp = request.form.get("t")
        humidity = request.form.get("h")
        ph_level = request.form.get("ph_level")
        rainfall = request.form.get("rainfall")

        # Importing our excel data from a specific file.
        excel = pd.read_excel('data/crop.xlsx', header=0)
        # Printing our excel file data.
        print(excel)
        print(excel.shape)

        # Various machine learning algorithms require numerical input data, so you need to represent categorical columns in a numerical column. In order to encode this data, you could map each value to a number. This process is known as label encoding, and sklearn conveniently will do this for you using Label Encoder.
        le = preprocessing.LabelEncoder()
        crop = le.fit_transform(list(excel["CROP"]))

        # Making the whole row consisting of nitrogen values to come into nitrogen.
        NITROGEN = list(excel["NITROGEN"])
        # Making the whole row consisting of phosphorus values to come into phosphorus.
        PHOSPHORUS = list(excel["PHOSPHORUS"])
        # Making the whole row consisting of potassium values to come into potassium.
        POTASSIUM = list(excel["POTASSIUM"])
        # Making the whole row consisting of temperature values to come into temperature.
        TEMPERATURE = list(excel["TEMPERATURE"])
        # Making the whole row consisting of humidity values to come into humidity.
        HUMIDITY = list(excel["HUMIDITY"])
        # Making the whole row consisting of ph values to come into ph.
        PH = list(excel["PH"])
        RAINFALL = list(excel["RAINFALL"])

        # Zipping all the features together
        features = list(zip(NITROGEN, PHOSPHORUS, POTASSIUM,
                    TEMPERATURE, HUMIDITY, PH, RAINFALL))
        features = np.array([NITROGEN, PHOSPHORUS, POTASSIUM,
                        TEMPERATURE, HUMIDITY, PH, RAINFALL])

        # Making transpose of the features
        features = features.transpose()
        # Printing the shape of the features after getting transposed.
        print(features.shape)
        print(crop.shape)

        # The number of neighbors is the core deciding factor. K is generally an odd number if the number of classes is 2. When K=1, then the algorithm is known as the nearest neighbor algorithm.
        model = KNeighborsClassifier(n_neighbors=3)
        model.fit(features, crop)

        data = np.array([[nitrogen, phosphorus, potassium, temp, humidity, ph_level, rainfall]])

        c = np.array(data, dtype=float) #  convert with for loop
        # predict1 = model.predict(data)
        predict1 = model.predict(c)
        print(predict1)

        crop_name = str()
        if predict1 == 0:
            crop_name = 'Apple(सेब)'
        elif predict1 == 1:
           crop_name = 'Banana(केला)'
        elif predict1 == 2:
           crop_name = 'Blackgram(काला चना)'
        elif predict1 == 3:
           crop_name = 'Chickpea(काबुली चना)'
        elif predict1 == 4:
           crop_name = 'Coconut(नारियल)'
        elif predict1 == 5:
           crop_name = 'Coffee(कॉफ़ी)'
        elif predict1 == 6:
           crop_name = 'Cotton(कपास)'
        elif predict1 == 7:
            crop_name = 'Grapes(अंगूर)'
        elif predict1 == 8:
            crop_name = 'Jute(जूट)'
        elif predict1 == 9:
            crop_name = 'Kidneybeans(राज़में)'
        elif predict1 == 10:
            crop_name = 'Lentil(मसूर की दाल)'
        elif predict1 == 11:
            crop_name = 'Maize(मक्का)'
        elif predict1 == 12:
            crop_name = 'Mango(आम)'
        elif predict1 == 13:
            crop_name = 'Mothbeans(मोठबीन)'
        elif predict1 == 14:
            crop_name = 'Mungbeans(मूंग)'
        elif predict1 == 15:
            crop_name = 'Muskmelon(खरबूजा)'
        elif predict1 == 16:
            crop_name = 'Orange(संतरा)'
        elif predict1 == 17:
            crop_name = 'Papaya(पपीता)'
        elif predict1 == 18:
            crop_name = 'Pigeonpeas(कबूतर के मटर)'
        elif predict1 == 19:
            crop_name = 'Pomegranate(अनार)'
        elif predict1 == 20:
            crop_name = 'Rice(चावल)'
        elif predict1 == 21:
            crop_name = 'Watermelon(तरबूज)'
        print(crop_name)
        # ans =  Markup(str(crop_name))
        #return "Suggested crop: " + crop_name
        return render_template('recommender-result.html', crop_name = crop_name)

    else:
         return render_template('fail.html')
    


if __name__ == "__main__":
    app.run(debug=True)
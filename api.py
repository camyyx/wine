from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import joblib
import uvicorn
import sklearn

app = FastAPI()
model1 = joblib.load("knn.pkl")
model2 = joblib.load("dt.pkl")

class Wine(BaseModel):
    fixed_acidity =  float
    volatile_acidity =  float
    citric_acid =  float
    residual_sugar =  float
    chlorides =  float 
    free_sulfur_dioxide =  float
    total_sulfur_dioxide =  float
    density =  float
    pH =  float
    sulphates =  float
    alcohol =  float
    wine_type = int

@app.post("/knn")
def classmodel1(wine:Wine):
    X = pd.DataFrame({
     'id' :  [8000],
     'fixed_acidity' :[wine.fixed_acidity],
     'volatile_acidity' : [wine.volatile_acidity],
     'citric_acid' :  [wine.citric_acid],
     'residual_sugar' :  [wine.residual_sugar],
     'chlorides' :  [wine.chlorides], 
     'free_sulfur_dioxide' : [wine.free_sulfur_dioxide],
     'total_sulfur_dioxide' :  [wine.total_sulfur_dioxide],
     'density' :  [wine.density],
     'pH' :  [wine.pH],
     'sulphates' :  [wine.sulphates],
     'alcohol' : [wine.alcohol],
     'wine_type' :  [wine.wine_type]
    })
    Y_pred = model1.predict(X)[0]
    
    return Y_pred


@app.post("/dt")
def classmodel2(wine:Wine):
    X = pd.DataFrame({
     'id' :  [8000],
     'fixed_acidity' :[wine.fixed_acidity],
     'volatile_acidity' : [wine.volatile_acidity],
     'citric_acid' :  [wine.citric_acid],
     'residual_sugar' :  [wine.residual_sugar],
     'chlorides' :  [wine.chlorides], 
     'free_sulfur_dioxide' : [wine.free_sulfur_dioxide],
     'total_sulfur_dioxide' :  [wine.total_sulfur_dioxide],
     'density' :  [wine.density],
     'pH' :  [wine.pH],
     'sulphates' :  [wine.sulphates],
     'alcohol' : [wine.alcohol],
     'wine_type' :  [wine.wine_type]
    })
    Y_pred = model2.predict(X)[0]
    
    return Y_pred


if __name__ == '__main__' :
    uvicorn.run(app,host="0.0.0.0",port="8000")
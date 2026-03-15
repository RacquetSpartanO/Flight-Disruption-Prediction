import pandas as pd
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
import numpy as np
import joblib

file = pd.read_csv(r"D:\DP project\IV SEM\Thinkathon\flight_delay_dataset.csv")

X = file.drop('delay', axis='columns')
Y = file.delay

column_trans = make_column_transformer((StandardScaler(),['time_to_departure', 'boarding_progress']), remainder='passthrough')
logreg = LogisticRegression(solver='lbfgs')

pipe = make_pipeline(column_trans, logreg)

print(cross_val_score(pipe, X, Y, cv=5, scoring='accuracy').mean())

pipe.fit(X,Y)

joblib.dump(pipe, r"D:\DP project\IV SEM\Thinkathon\flightdelay_pred_model.pkl")
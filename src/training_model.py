
import pandas as pd

from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score, confusion_matrix, recall_score, 
    plot_confusion_matrix, precision_score, plot_roc_curve
)

from sklearn.ensemble import RandomForestClassifier
from joblib import dump

from storage import Storage 

storage = Storage()
storage.download("../data/output/train_model.csv","output/train_model.csv")

df = pd.read_csv('../data/output/train_model.csv')
cust_df = df.copy()
cust_df.fillna(0, inplace=True)
Y = cust_df['status'].astype('int')

cust_df.drop(['status'], axis=1, inplace=True)
cust_df.drop(['id'], axis=1, inplace=True)

X = cust_df
X_train, X_test, y_train, y_test = train_test_split(X, Y, 
                                                    stratify=Y, test_size=0.3,
                                                    random_state = 123)
# Using Synthetic Minority Over-Sampling Technique(SMOTE) to overcome sample imbalance problem.
#Y = Y.astype('int')

X_train, y_train = SMOTE().fit_resample(X_train, y_train)
X_train = pd.DataFrame(X_train, columns=X.columns)
model = RandomForestClassifier(n_estimators=5)

model.fit(X_train, y_train)
y_predict = model.predict(X_test)

print('Accuracy Score is {:.5}'.format(accuracy_score(y_test, y_predict)))
print('Precision Score is {:.5}'.format(precision_score(y_test, y_predict)))
print('Recall Score is {:.5}'.format(precision_score(y_test, y_predict)))
print(pd.DataFrame(confusion_matrix(y_test,y_predict)))

plot_confusion_matrix(model, X_test, y_test) 
plot_roc_curve(model, X_test, y_test)

dump(model, '../train_models/model_risk.joblib') 

storage.upload('../train_models/model_risk.joblib','train_models/model_risk.joblib')

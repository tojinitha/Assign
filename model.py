import pandas as pd 
import pickle
train = pd.read_csv('train1.csv')

from sklearn.model_selection import train_test_split



X_train = train.drop(['satisfaction','Class_Eco','Class_Eco Plus','Type of Travel_Personal Travel'],axis=1)
y_train=train['satisfaction']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.2, random_state=42)

import lightgbm as lgb
from lightgbm import LGBMClassifier
model = LGBMClassifier()
model.fit(X_train, y_train)
 


#saving model to disk
pickle.dump(model,open('model.pkl','wb'))
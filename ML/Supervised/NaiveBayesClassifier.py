# -*- coding: utf-8 -*-
"""NaiveBayesClassifier.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19A2_I_zT28V0cLETTq-FOIVHSSMl7B-k
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, LabelEncoder, StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

data = pd.read_csv(r'D:\CODING_CODES\AIML\ML\Supervised\Data\classification_decision_tree_dataset.csv')

print(data.columns)

print(data.sample(10))

print(data.isna().sum())

print(data['Education'].value_counts())
print(data['Marital_Status'].value_counts())

X = data.drop(['Purchase'],axis=1)
y = data['Purchase']

transformer = ColumnTransformer(transformers=[
    ('tnf1',OrdinalEncoder(categories=[['High School','Bachelor','Master','PhD']]),['Education']),
    ('tnf2',OneHotEncoder(drop='first',sparse_output=False,dtype=np.int32),['Marital_Status'])
],remainder='passthrough')

X_modified = transformer.fit_transform(X)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_modified)

X_train, X_test, y_train, y_test = train_test_split(X_scaled,y,test_size = 0.2, random_state = 3)

naive = GaussianNB()

naive.fit(X_train,y_train)

accuracy = accuracy_score(y_test,naive.predict(X_test))
print(accuracy)

print(y_test)

print(naive.predict(X_test))


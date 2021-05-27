# -*- coding: utf-8 -*-
"""Day5_HandwrittenDigitRecognition_SVM.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EK2eiDs7ikLf1T0zSulcowcAiy0S8Yri

# **Day - 5 | Handwritten Digit Recognition | SVM**

### *Importing Basic Libraries*
"""

import numpy as np
from sklearn.datasets import load_digits

"""### *Load Dataset*
![image.png](data:image/png;base64,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)
"""

dataset = load_digits()

"""### *Summarize Dataset*"""

print(dataset.data)
print(dataset.target)

print(dataset.data.shape)
print(dataset.images.shape)

dataimageLength = len(dataset.images)
print(dataimageLength)

"""### *Visualize the Dataset*"""

n=9 #No. of Sample out of Samples total 1797

import matplotlib.pyplot as plt
plt.gray()
plt.matshow(dataset.images[n])
plt.show()

dataset.images[n]

"""### *Segregate Dataset into X(Input/IndependentVariable) & Y(Output/DependentVariable)*

### *Input - Pixel | Output - Class*
"""

X = dataset.images.reshape((dataimageLength,-1))
X

Y = dataset.target
Y

"""### *Splitting Dataset into Train & Test*"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.25, random_state = 0)
print(X_train.shape)
print(X_test.shape)

"""### *Training*"""

from sklearn import svm
model = svm.SVC(kernel='linear')
model.fit(X_train,y_train)

"""### *Predicting, what the digit is from Test Data*"""

n=13
result = model.predict(dataset.images[n].reshape((1,-1)))
plt.imshow(dataset.images[n], cmap=plt.cm.gray_r, interpolation='nearest')     
print(result)
print("\n")
plt.axis('off')
plt.title('%i' %result)
plt.show()

"""### *Prediction for Test Data*"""

y_pred = model.predict(X_test)
print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))

"""### *Evaluate Model - Accuracy Score*"""

from sklearn.metrics import accuracy_score
print("Accuracy of the Model: {0}%".format(accuracy_score(y_test, y_pred)*100))

"""### *Play with the Different Method*"""

from sklearn import svm
model1 = svm.SVC(kernel='linear')
model2 = svm.SVC(kernel='rbf')
model3 = svm.SVC(gamma=0.001)
model4 = svm.SVC(gamma=0.001,C=0.1)

model1.fit(X_train,y_train)
model2.fit(X_train,y_train)
model3.fit(X_train,y_train)
model4.fit(X_train,y_train)

y_predModel1 = model1.predict(X_test)
y_predModel2 = model2.predict(X_test)
y_predModel3 = model3.predict(X_test)
y_predModel4 = model4.predict(X_test)

print("Accuracy of the Model 1: {0}%".format(accuracy_score(y_test, y_predModel1)*100))
print("Accuracy of the Model 2: {0}%".format(accuracy_score(y_test, y_predModel2)*100))
print("Accuracy of the Model 3: {0}%".format(accuracy_score(y_test, y_predModel3)*100))
print("Accuracy of the Model 4: {0}%".format(accuracy_score(y_test, y_predModel4)*100))
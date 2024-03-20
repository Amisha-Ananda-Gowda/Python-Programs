from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn import datasets
iris=datasets.load_iris()
x=iris.data
y=iris.target
print('Sepal-length','Sepal-width','Petal-length','Petal-width')
print(x)
print('Class:0-Iris-Setosa,1-Iris-Virginica,2-Iris-Versicolor')
print(y)
x_train,x_test,y_train,y_test=train_test_split(test_size=0.3)
classifier=KNeighborsClassifier(n_neighbors=5)
classifier.fit(x_train,y_train)
ypred=classifier.predict(x_test)
print("Confusion Matrix")
print(confusion_matrix(y_test,y_pred))
print("Accuracy Matrix")
print(classification_report(y_test,y_pred))

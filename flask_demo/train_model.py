from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np
import pickle

np.random.seed(42)

# Load the dataset
iris = load_iris()
X = iris.data
y = iris.target

# Train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.2)

# Build the model
clf = RandomForestClassifier(n_estimators=10)

# Train the classifier
clf.fit(X_train, y_train)

# Prodictions
predicted = clf.predict(X_test)

# Check Accuracy
print(f'Model\'s accuracy: {accuracy_score(y_test, predicted)}')

# Save the model
with open('my_model.pkl', 'wb') as f:
    pickle.dump(clf, f)

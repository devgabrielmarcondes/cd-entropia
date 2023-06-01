import pandas as pd
from math import log2
from sklearn.neighbors import KNeighborsClassifier # KNN

# Laptop price prediction data
data = pd.read_csv('laptops_train.csv')

# Testing laptop data set
test = pd.read_csv('laptops_test.csv')

# Discretize quantitative data
def discretizeColumn(column, testColumn):
    knn = KNeighborsClassifier(n_neighbors=10)
    columnValues = column.values.reshape(-1, 1)
    labels = pd.qcut(columnValues.flatten(), q=10, labels=False, duplicates='drop')
    knn.fit(columnValues, labels)
    testColumnValues = testColumn.values.reshape(-1, 1)
    discretizedValues = knn.predict(testColumnValues)
    return discretizedValues

# Calculates the entropy of each column

def allEntropy():
    for colName in data.columns:
        column = data[colName]
        testColumn = test[colName]
        if column.dtype == 'object':
            # Categorical column
            classes = column.value_counts()
            probabilities = classes / len(data)
            
            # Entropy
            eachEntropy = 0
            for p in probabilities:
                eachEntropy += -p * log2(p)
            maxEachEntropy = log2(len(probabilities))
        else:
            # Quantitative column
            discColumn = discretizeColumn(column,testColumn)
            classes = pd.Series(discColumn).value_counts()
            probabilities = classes / len(test)
            eachEntropy = 0
            for p in probabilities:
                eachEntropy += -p * log2(p)
            maxEachEntropy = log2(len(probabilities))

        print(f"Entropy of the column {colName}: {eachEntropy}. Maximum: {maxEachEntropy}")

allEntropy()
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
import pickle

def train_test_split(data, ratio):

    np.random.seed(56)
    shuffled = np.random.permutation(len(data))
    test_set_size = int(len(data)*ratio)
    test_indices = shuffled[:test_set_size]
    train_indices = shuffled[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]


if __name__ == '__main__':
    
    df = pd.read_csv("C:/Users/91741/Desktop/myproject/data.csv")
    train, test = train_test_split(df, 0.2)

    x_train = train[['fever','bodyPain','age','runnyNose','diffBreath']].to_numpy()
    x_test = test[['fever','bodyPain','age','runnyNose','diffBreath']].to_numpy()

    y_train = train[['infectionProb']].to_numpy().reshape(2060,)
    y_test = test[['infectionProb']].to_numpy().reshape(515,)

    
    clf = LogisticRegression()
    clf.fit(x_train, y_train)

    file = open('model.pkl','wb')
    pickle.dump(clf,file)
    file.close()

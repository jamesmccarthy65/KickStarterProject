import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
import sklearn
from sklearn.externals import joblib


def dtParamSelect(X_train, y_train):
    model = DecisionTreeClassifier()
    params = {
        'criterion': ['gini', 'entropy'],
        'max_depth': [5, 10, 15, 20],
        'min_samples_split': [25, 50, 100, 250, 500, 1000],
        'random_state': [0]
    }
    gd_sr = GridSearchCV(estimator=model,
                         param_grid=params,
                         scoring='f1',
                         cv=10,
                         n_jobs=-1)
    gd_sr.fit(X_train, y_train)
    joblib.dump(gd_sr, 'dtParams.pkl')
    return gd_sr.best_params_


def lgrParamSelect(X_train, y_train):
    model = LogisticRegression()
    params = {
        'solver': ['sag', 'lbfgs'],
        'C': [0.0001, 0.001, 0.01, 0.1, 1, 2]
    }
    gd_sr = GridSearchCV(estimator=model,
                         param_grid=params,
                         scoring='accuracy',
                         cv=10,
                         n_jobs=-1)

    gd_sr.fit(X_train, y_train)
    joblib.dump(gd_sr, './ModelHyperparm/lgrParams.pkl')
    return gd_sr.best_params_


def knnParamSelect(X_train, y_train):
    model = KNeighborsClassifier()
    params = {
        'n_neighbors': [5, 10, 20],
        'weights': ['uniform', 'distance'],
        'algorithm': ['ball_tree', 'kd_tree'],
        'p': [1, 2],
        'n_jobs': [-1]
    }
    gd_sr = GridSearchCV(estimator=model,
                         param_grid=params,
                         scoring='f1',
                         cv=10,
                         n_jobs=-1)
    gd_sr.fit(X_train, y_train)
    joblib.dump(gd_sr, './ModelHyperparm/knnParams.pkl')
    return gd_sr.best_params_

import math
import pickle
import re

import numpy as np
import pandas as pd

from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.cluster import KMeans, Birch, DBSCAN
from imblearn.over_sampling import RandomOverSampler, SMOTE
from imblearn.under_sampling import RandomUnderSampler

class ClusteringModel:
    def __init__(self, verbose=True):
        self.verbose = verbose

    def get_data(self, df):
        self.df = df
        self.sentences = self.df['Content']
        self.labels = self.df['Match']

    def embed(self, embedding_path=None):
        if embedding_path is not None:
            if self.verbose:
                print('Loading embeddings...')
            with open(embedding_path, "rb") as handle:
                self.embeddings = pickle.load(handle)['embeddings']
                if self.verbose:
                    print('Embeddings loaded from', embedding_path)

    def create_model(self, model_type='svc'):
        if model_type == 'svc':
            self.model = DBSCAN(eps=0.3, min_samples=11, n_jobs=-1)


    def fit_model(self, test_size=0.2, resample='smote'):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.embeddings, self.labels,
                                                                                test_size=test_size,
                                                                                shuffle=True, random_state=0)
        if resample == 'ros':
            ros = RandomOverSampler(random_state=0)
            self.X_train, self.y_train = ros.fit_resample(self.X_train, self.y_train)
        elif resample == 'smote':
            smote = SMOTE(random_state=0)
            self.X_train, self.y_train = smote.fit_resample(self.X_train, self.y_train)
        elif resample == 'rus':
            rus = RandomUnderSampler(random_state=0)
            self.X_train, self.y_train = rus.fit_resample(self.X_train, self.y_train)


        self.model.fit(self.X_train, self.y_train)

    def evaluate_model(self):
        y_test_pred = self.model.predict(self.X_test)
        print(classification_report(y_true=self.y_test, y_pred=y_test_pred))

    def predict_model(self, X):
        return self.model.predict(X)

    def load_model(self, model_path):
        with open(model_path, 'rb') as handle:
            self.model = pickle.load(handle)
        if self.verbose:
            print('Model loaded from', model_path)

    def save_model(self, model_path):
        with open(model_path, 'wb') as handle:
            pickle.dump(self.model, handle)
        if self.verbose:
            print('Model saved to', model_path)
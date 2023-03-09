import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score
from imblearn.over_sampling import RandomOverSampler

class RelevanceModel:
    def __init__(self):
        self.model = None
        self.vectorizer = None

    def train_model(self):

        # split into X and y
        X = df['query'].values
        y = df['relevance'].values

        # vectorize X
        pipeline = Pipeline([
            ('vectorizer', TfidfVectorizer()),
            ('oversampler', RandomOverSampler()),
            ('clf', RandomForestClassifier())
        ])

        parameters = {
            'vectorizer__ngram_range': [(1,1), (1,2)],
            'clf__n_estimators': [100, 200, 500],
            'clf__max_depth': [10, 50, None],
            'clf__min_samples_leaf': [1, 2, 4]
        }

        grid_search = GridSearchCV(pipeline, parameters, cv=5, n_jobs=-1)
        grid_search.fit(X, y)

        # evaluate the model
        y_pred = grid_search.predict(X)
        accuracy = accuracy_score(y, y_pred)
        print("Model accuracy:", accuracy)

        # save the model
        with open('model.pkl', 'wb') as f:
            pickle.dump(grid_search, f)

        self.model = grid_search
        self.vectorizer = grid_search.best_estimator_.named_steps['vectorizer']

    def query_results_by_relevance(self, query):
        query_vector = self.vectorizer.transform([query])
        relevance_scores = self.model.predict_proba(query_vector)[:,1]
        links_with_scores = zip(links, relevance_scores)

        # sort links by relevance score
        sorted_links = sorted(links_with_scores, key=lambda x: x[1], reverse=True)
        sorted_links = [x[0] for x in sorted_links]

        return sorted_links

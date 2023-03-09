import pandas as pd
import spacy
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from imblearn.pipeline import Pipeline as ImbPipeline
from imblearn.over_sampling import SMOTE
from collections import Counter
import pickle

class RelevancePredictor:
    
    def __init__(self):
        with open('model.pkl', 'rb') as f:
            self.model = pickle.load(f)
        self.db = pd.read_csv('database.csv')
        self.preprocess_pipeline = Pipeline([
            ('spacy', spacy.load('en_core_web_sm', disable=['parser', 'ner'])),
            ('vectorizer', CountVectorizer(tokenizer=lambda x: x, lowercase=False)),
            ('tfidf', TfidfTransformer())
        ])
        
    def train_model(self):
        train_df = self.db.sample(frac=0.8, random_state=42)
        test_df = self.db.drop(train_df.index)
        pipeline = Pipeline([
            ('preprocess', self.preprocess_pipeline),
            ('model', LogisticRegression(random_state=42))
        ])
        parameters = {'model__C': [0.1, 1, 10]}
        clf = GridSearchCV(pipeline, parameters, cv=5)
        clf.fit(train_df['text'], train_df['label'])
        score = clf.score(test_df['text'], test_df['label'])
        print(f"Accuracy: {score:.4f}")
        with open('model.pkl', 'wb') as f:
            pickle.dump(clf.best_estimator_, f)
        self.model = clf.best_estimator_
        
    def query_results_by_relevance(self, query):
        query_vec = self.preprocess_pipeline.transform([query])
        link_scores = self.model.predict_proba(self.db['text'])[:, 1]
        sorted_links = self.db.iloc[link_scores.argsort()[::-1]]
        return sorted_links.to_dict('records')

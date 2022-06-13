from sklearn import svm
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline

classifier = svm.LinearSVC(C=1.0, class_weight="balanced")
model = Pipeline([ 
      ('translate', EnglishTransformer()),
      ('tfidf', TfidfVectorizer()), 
      ("classifier", classifier) 
])
import numpy as np
import pandas as pd
from nltk.stem import PorterStemmer
def get_model():
    df=pd.read_csv('movie data/moviedata.csv')
    import re
    filterdata=[]
    for i in df['review']:
        i=i.lower()
        i=i.replace('[','')
        i=i.replace(']','')
        i=i.replace('(','')
        i=i.replace(')','')
        i=i.replace('{','')
        i=i.replace('}','')
        i=i.replace('[','')
        i=i.replace("%d+",'')
        i=i.replace('[--]+','')
        i=re.sub('[^A-za-z ]',"",i)
        filterdata.append(i)
    filterdata[:5]
    newtext=[]
    stop=['i', 'me', 'my', 'myself', 'we', 'our', 'ours',' br', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now',]
    for i in filterdata:
        text = i.split()
        ntext=''
        for word in text:
            if word in stop:
                pass
            else:
                ntext+=" "+word
        newtext.append(ntext)
    df['cleaned_text']=newtext
    ps=PorterStemmer()
    cleaned_data=[ps.stem(word) for word in df['cleaned_text']]
    print(cleaned_data[:5])
    x=cleaned_data
    y=df['sentiment']
    from sklearn.model_selection import train_test_split
    xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.1,random_state=48)
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.linear_model import LogisticRegression
    from sklearn.pipeline import Pipeline
    ob1=TfidfVectorizer()
    ob2=LogisticRegression()
    model=Pipeline([('vectorizer',ob1),('classifier',ob2)])
    model.fit(xtrain,ytrain)
    ypred=model.predict(xtest)
    from sklearn.metrics import accuracy_score
    print(accuracy_score(ypred,ytest))
    return model
def predictdata(data):
    model=get_model()
    res=model.predict(data)
    return res

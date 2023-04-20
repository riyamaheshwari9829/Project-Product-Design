import numpy as np
import pandas as pd
import re
def get_model():
    df=pd.read_csv('maildata/maildata.csv')
    filterdata=[]
    for i in df['Message']:
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
    stop=['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now',]

    for i in filterdata:
        text = i.split()
        ntext=''
        for word in text:
            if word in stop:
                pass
            else:
                ntext+=" "+word
        newtext.append(ntext)
    print(newtext[:5])
    df['cleaned_text']=newtext
    data1=pd.get_dummies(df['Category'])
    data1=data1.drop('spam',axis=1)
    data1=data1.rename(columns={'ham':'response'})
    data1.head()
    x=df['cleaned_text']
    y=data1['response']
    from sklearn.model_selection import train_test_split
    xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.15,random_state=42)
    print(len(xtrain),len(xtest))
    from sklearn.linear_model import LogisticRegression
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.pipeline import Pipeline
    ob1=LogisticRegression()
    ob2=TfidfVectorizer()
    model=Pipeline([('vectorizer',ob2),('classifier',ob1)])
    model.fit(xtrain,ytrain)
    model.fit(xtrain,ytrain)
    ypred=model.predict(xtest)
    from sklearn.metrics import accuracy_score
    print(accuracy_score(ypred,ytest))
    return model
def predictdata(data):
    model=get_model()
    res=model.predict(data)
    return res





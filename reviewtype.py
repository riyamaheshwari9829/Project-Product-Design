import numpy as np
import pandas as pd
def get_model():
    maildata=pd.read_csv('maildata/maildata.csv')
    hoteldata=pd.read_csv('hotel/train.csv')
    moviedata=pd.read_csv('movie data/moviedata.csv')
    moviedata=moviedata.head(5000)
    maildata=maildata.head(5000)
    hoteldata=hoteldata.head(5000)
    moviedata['category']=['movie']*5000
    maildata['category']=['mail']*5000
    hoteldata['category']=['hotel']*5000
    newdf=pd.concat([hoteldata['Description'],moviedata['review'],maildata['Message']],axis=0)
    newdf.shape
    newdf=pd.DataFrame(newdf,columns=['textdata'])
    newdf.head()
    newdf2=pd.concat([hoteldata['category'],moviedata['category'],maildata['category']],axis=0)
    finaldf=pd.concat([newdf,newdf2],axis=1)
    finaldf.head()
    import string as s
    filterdata=[]
    for i in finaldf['textdata']:
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
        i=i.translate(str.maketrans('', '', s.punctuation))
        filterdata.append(i)
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
    finaldf['cleaned_text']=newtext
    x=finaldf['cleaned_text']
    y=finaldf['category']
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
    print(ypred[:15])
    print(ytest[:15])
    from sklearn.metrics import accuracy_score
    print(accuracy_score(ypred,ytest))
    return model

def predictdata(data):
    model=get_model()
    res=model.predict(data)
    return res

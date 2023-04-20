import numpy as np
import pandas as pd
def get_model():
    df=pd.read_csv('hotel/train.csv')
    newdf=df.drop(['User_ID','Browser_Used','Device_Used'],axis=1)
    newdf.head()
    responsedata=pd.get_dummies(df['Is_Response'])
    responsedata.head()
    responsedata=responsedata.drop(['not happy'],axis=1)
    responsedata=responsedata.rename(columns={'happy':'response'})
    responsedata.head()
    newdf=newdf.drop(['Is_Response'],axis=1)
    newdata=pd.concat([newdf,responsedata],axis=1)
    newdata.head()
    import string as s
    filterdata=[]
    for i in newdata['Description']:
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
    df['cleaned_text']=newtext
    x=df['cleaned_text']
    y=df['Is_Response']
    print('all part done')
    from sklearn.model_selection import train_test_split
    xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.1,random_state=48)
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.linear_model import LogisticRegression
    from sklearn.pipeline import Pipeline
    ob1=TfidfVectorizer()
    ob2=LogisticRegression()
    print('modules imported')
    model=Pipeline([('vectorizer',ob1),('classifier',ob2)])
    model.fit(xtrain,ytrain)
    ypred=model.predict(xtest)
    print('model created')
    return model
def predictdata(data):
    model=get_model()
    res=model.predict(data)
    return res


    

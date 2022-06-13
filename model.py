#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[3]:


df=pd.read_csv('Training.csv')


# In[4]:





# In[5]:


X=df.drop('prognosis',axis=1)


# In[6]:





# In[7]:


y=df['prognosis']


# In[8]:





# In[9]:




# In[11]:


from sklearn.neural_network import MLPClassifier
mlp=MLPClassifier()
mlp.fit(X,y)


# In[12]:





# In[13]:




# In[29]:


indices = [i for i in range(133)]
symptoms = df.columns.values[:-1]
dictionary = dict(zip(symptoms,indices))
def predict_disease(symptom):
    user_input_symptoms = symptom
    user_input_label = [0 for i in range(133)]
    for i in user_input_symptoms:
        idx = dictionary[i]
        user_input_label[idx] = 1

    user_input_label = np.array(user_input_label)
    user_input_label = user_input_label.reshape((-1,1)).transpose()
    return(mlp.predict(user_input_label))


# In[32]:


a=predict_disease(['no','no','no'])
print(a[0])    







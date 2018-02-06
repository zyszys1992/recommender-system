#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 22:30:18 2018

@author: yishanzhang
"""
import pandas as pd
import numpy as np
import random
from functools import reduce


def get_train(path,train_num_percent):
    data=pd.read_csv(path, sep=',')
    train=random.sample(range(len(data.ix[:,1])),divmod(len(data.ix[:,1]),train_num_percent)[0])
    data_train=data.ix[train,].dropna().drop(['category1', 'category2'],1)
    data_train.index=range(len(data_train.ix[:,1]))
    customer_id=np.unique(data_train.client)
    l=list()
    for i in range(len(customer_id)):
        x=np.where(data_train.client==customer_id[i])[0]
        if len(x)>=2:l=l+x.tolist()
    data_train_2=data_train.loc[data_train.index[l],:]
    data_train_2.index=range(len(data_train_2.ix[:,1]))
    return data_train_2,l,data



def prefs(data_train_2):
    data_groups=data_train_2.groupby('client')
    customer_preferences=dict()
    for key,group in data_groups:
        group=group.sort_values(by='date_commande_client')
        famille_intitule=group['famille_intitule'].tolist()
        famille_intitule_len=len(group['famille_intitule'])
        prefer=dict()
        for i in range(famille_intitule_len):
            prefer[famille_intitule[i]]=1+prefer.get(famille_intitule[i],0)
            customer_preferences[key]=prefer
            n=len(customer_preferences[key].keys())
            par=reduce(lambda x,y: x+y, range(n+1))
            i=n
        for key2 in customer_preferences[key]:
            customer_preferences[key][key2]=customer_preferences[key][key2]*i/par
            i=i-1
    return customer_preferences
    

def prefs_future(data,l):
    data_test=data.drop(data.index[l])
    data_test=data_test.drop(['category1', 'category2'],1)
    customer_preferences_future=dict()  
    data_test_groups=data_test.groupby('client')
    for key,group in data_test_groups:
        group=group.sort_values(by='date_commande_client')
        famille_intitule=group['famille_intitule'].tolist()
        famille_intitule_len=len(group['famille_intitule'])
        prefer=dict()
        for i in range(famille_intitule_len):
            prefer[famille_intitule[i]]=1+prefer.get(famille_intitule[i],0)
            customer_preferences_future[key]=prefer
            n=len(customer_preferences_future[key].keys())
            par=reduce(lambda x,y: x+y, range(n+1))
            i=n
        for key2 in customer_preferences_future[key]:
            customer_preferences_future[key][key2]=customer_preferences_future[key][key2]*i/par
            i=i-1
    return customer_preferences_future

if __name__=="__main__":
    get_train()
    prefs()
    prefs_future()           
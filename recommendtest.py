#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 23:27:15 2018

@author: yishanzhang
"""

from rdsys.recommendation import getRecommendations
import operator
import numpy as np

def recommend_test(train_prefs, test_prefs, n):
    prop=[]
    for customer in test_prefs:
        x=sorted(test_prefs[customer].items(), key=operator.itemgetter(1),reverse=True)[:n]
        x=[a[0] for a in x]
        try:
            getRecommendations(train_prefs,customer)[0][1]
            y=getRecommendations(train_prefs,customer)[:n]
            z=[b[1] for b in y]
            if set(x) & set(z): prop.append(1)
            else: prop.append(0)
        except:
            continue
    return np.mean(prop)

if __name__=="__main__":
    recommend_test()
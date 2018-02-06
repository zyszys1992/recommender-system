#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 22:47:09 2018

@author: yishanzhang
"""
import numpy as np

def pearson(prefs,pers1,pers2):
    si={}
    for item in prefs[pers1]:
        if item in prefs[pers2]:
            si[item]=1 
    n=len(si)
    if n==0: return 0
    sum1=sum([prefs[pers1][it] for it in si])
    sum2=sum([prefs[pers2][it] for it in si])
    sum1Sq=sum([pow(prefs[pers1][it],2) for it in si])
    sum2Sq=sum([pow(prefs[pers2][it],2) for it in si])
    psum=sum([prefs[pers1][it]*prefs[pers2][it] for it in si])
    num=psum-(sum1*sum2/n)
    den=np.sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
    if den==0: return 0
    r=abs(num/den)
    return r

if __name__=="__main__":
    pearson()
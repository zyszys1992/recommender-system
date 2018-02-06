#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 22:25:30 2018

@author: yishanzhang
"""
from rdsys.gettrain import get_train,prefs,prefs_future
from rdsys.recommendation import getRecommendations
from rdsys.recommendtest import recommend_test

class rdsy:
    def __init__(self,train_num_percent,path):
        self.train_num_percent=train_num_percent
        self.path=path
       
    
    def get_train_data(self):
        return get_train(self.path,self.train_num_percent)[0].head()
   
    def rcmd(self,person):
         t=get_train(self.path,self.train_num_percent)
         p=prefs(t[0])
         return getRecommendations(p,person)
    
    def test_data(self,n):
        t=get_train(self.path,self.train_num_percent)
        p=prefs(t[0])
        p_f=prefs_future(t[2],t[1])
        return recommend_test(p,p_f,n)

if __name__=="__main__":
    rdsy
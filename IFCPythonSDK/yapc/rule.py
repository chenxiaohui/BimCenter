#!/usr/bin/python
#coding=utf-8
#Filename:rule.py
from serializable import Serializable
class Rule(Serializable):
    """"""
    def __init__(self):
        super(Rule,self).__init__()
        self.target=''
        self.local={}      
        self.code={}


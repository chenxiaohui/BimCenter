#!/usr/bin/python
#coding=utf-8
#Filename:dataset.py

class DataSet(object):
    """"""
    def __init__(self):
        super(DataSet,self).__init__()
        self.header=''
        self.schemaName=''
        self.types={}       
        self.rules={}       
        self.entities={}       
        self.functions={}      

    def addRule(self,rule):
        """"""
        self.rules.append(rule)

    def addFunction(self,function):
        """"""
        self.functions.append(function)

    def addEntity(self,entity):
        """"""
        self.entities.append(entity)

    def addType(self,type):
        """"""
        self.types.append(type)

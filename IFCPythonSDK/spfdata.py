#!/usr/bin/python
#coding=utf-8
#Filename:SPFData.py
from utils import parseList

class SPFData(object):
    """"""
    def __init__(self):
        super(SPFData,self).__init__()
        self.index=-1
        self.argv=[]
        self.inverses={}

    def getInverses(self,cl,attr):
        """"""
        return self.inverses[(cl,attr)] if (cl,attr) in self.inverses else None 
    
    def addInverse(self,cl,attr,id):
        """"""
        if (cl,attr) in self.inverses:
            self.inverses[(cl,attr)].append(id)
        else:
            self.inverses[(cl,attr)]=[id]

    def setParams(self,s):
        """"""
        v=parseList(s)
        if not v:
            return False
        self.argv=v
        self.index=-1
        return True

    def getNext(self):
        """"""
        if self.index>=len(self.argv):
            return ''
        else :
            self.index+=1
            return self.argv[self.index]

    def argc(self):
        """"""
        return len(self.argv) 

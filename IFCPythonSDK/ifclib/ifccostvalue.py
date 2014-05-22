#!/usr/bin/python
#coding=utf-8
#Filename:IfcCostValue.py
import log
import common
from ifcappliedvalue import IFCAPPLIEDVALUE

from utils import *

class IFCCOSTVALUE(IFCAPPLIEDVALUE):
    """"""
    def __init__(self,id,arg):
        super(IFCCOSTVALUE,self).__init__(id,arg)
        self.type='IFCCOSTVALUE'
        self.inverse={}
        self.CostType=None #IfcLabel
        self.Condition=None #IfcText


    def load(self):
        """register inverses"""
        if not super(IFCCOSTVALUE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCOSTVALUE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.CostType= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Condition= fromSPF(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCOSTVALUE,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCCOSTVALUE,self).toString()       
        line += strToSPF(self.CostType)+','
        line += strToSPF(self.Condition)+','

        return line

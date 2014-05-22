#!/usr/bin/python
#coding=utf-8
#Filename:IfcConditionCriterion.py
import log
import common
from ifccontrol import IFCCONTROL

from utils import *

class IFCCONDITIONCRITERION(IFCCONTROL):
    """"""
    def __init__(self,id,arg):
        super(IFCCONDITIONCRITERION,self).__init__(id,arg)
        self.type='IFCCONDITIONCRITERION'
        self.inverse={}
        self.Criterion=None #IfcConditionCriterionSelect
        self.CriterionDateTime=None #IfcDateTimeSelect


    def load(self):
        """register inverses"""
        if not super(IFCCONDITIONCRITERION,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCONDITIONCRITERION,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Criterion= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.CriterionDateTime= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCONDITIONCRITERION,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCCONDITIONCRITERION,self).toString()       
        line += typerefToSPF(self.Criterion)+','
        line += typerefToSPF(self.CriterionDateTime)+','

        return line

#!/usr/bin/python
#coding=utf-8
#Filename:IfcDimensionCurveTerminator.py
import log
import common
from ifcterminatorsymbol import IFCTERMINATORSYMBOL

from utils import *

class IFCDIMENSIONCURVETERMINATOR(IFCTERMINATORSYMBOL):
    """"""
    def __init__(self,id,arg):
        super(IFCDIMENSIONCURVETERMINATOR,self).__init__(id,arg)
        self.type='IFCDIMENSIONCURVETERMINATOR'
        self.inverse={}
        self.Role=None #IfcDimensionExtentUsage


    def load(self):
        """register inverses"""
        if not super(IFCDIMENSIONCURVETERMINATOR,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCDIMENSIONCURVETERMINATOR,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Role= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCDIMENSIONCURVETERMINATOR,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCDIMENSIONCURVETERMINATOR,self).toString()       
        line += typerefToSPF(self.Role)+','

        return line

#!/usr/bin/python
#coding=utf-8
#Filename:IfcRationalBezierCurve.py
import log
import common
from ifcbeziercurve import IFCBEZIERCURVE

from utils import *

class IFCRATIONALBEZIERCURVE(IFCBEZIERCURVE):
    """"""
    def __init__(self,id,arg):
        super(IFCRATIONALBEZIERCURVE,self).__init__(id,arg)
        self.type='IFCRATIONALBEZIERCURVE'
        self.inverse={}
        self.WeightsData=None #LIST


    def load(self):
        """register inverses"""
        if not super(IFCRATIONALBEZIERCURVE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCRATIONALBEZIERCURVE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.WeightsData= getIdListParam(arg,spfToInteger)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCRATIONALBEZIERCURVE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCRATIONALBEZIERCURVE,self).toString()       
        line += listParamToSPF(self.WeightsData,integerToSPF)+','

        return line

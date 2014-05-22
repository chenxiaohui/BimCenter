#!/usr/bin/python
#coding=utf-8
#Filename:IfcDimensionCurve.py
import log
import common
from ifcannotationcurveoccurrence import IFCANNOTATIONCURVEOCCURRENCE

from utils import *

class IFCDIMENSIONCURVE(IFCANNOTATIONCURVEOCCURRENCE):
    """"""
    def __init__(self,id,arg):
        super(IFCDIMENSIONCURVE,self).__init__(id,arg)
        self.type='IFCDIMENSIONCURVE'
        self.inverse={}
        self.inverse['AnnotatedBySymbols']=[] #inverse:SET of IfcTerminatorSymbol


    def load(self):
        """register inverses"""
        if not super(IFCDIMENSIONCURVE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCDIMENSIONCURVE,self).init():
            return False

        inverses = self.args.getInverses('IFCTERMINATORSYMBOL', 'AnnotatedCurve');
        if inverses:
            self.inverse['AnnotatedBySymbols']=inverses

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCDIMENSIONCURVE,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCDIMENSIONCURVE,self).toString()       

        return line

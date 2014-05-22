#!/usr/bin/python
#coding=utf-8
#Filename:IfcCenterLineProfileDef.py
import log
import common
from ifcarbitraryopenprofiledef import IFCARBITRARYOPENPROFILEDEF

from utils import *

class IFCCENTERLINEPROFILEDEF(IFCARBITRARYOPENPROFILEDEF):
    """"""
    def __init__(self,id,arg):
        super(IFCCENTERLINEPROFILEDEF,self).__init__(id,arg)
        self.type='IFCCENTERLINEPROFILEDEF'
        self.inverse={}
        self.Thickness=None #IfcPositiveLengthMeasure


    def load(self):
        """register inverses"""
        if not super(IFCCENTERLINEPROFILEDEF,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCENTERLINEPROFILEDEF,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Thickness= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCENTERLINEPROFILEDEF,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCCENTERLINEPROFILEDEF,self).toString()       
        line += integerToSPF(self.Thickness)+','

        return line

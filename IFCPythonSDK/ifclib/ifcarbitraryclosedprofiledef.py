#!/usr/bin/python
#coding=utf-8
#Filename:IfcArbitraryClosedProfileDef.py
import log
import common
from ifcprofiledef import IFCPROFILEDEF

from utils import *

class IFCARBITRARYCLOSEDPROFILEDEF(IFCPROFILEDEF):
    """"""
    def __init__(self,id,arg):
        super(IFCARBITRARYCLOSEDPROFILEDEF,self).__init__(id,arg)
        self.type='IFCARBITRARYCLOSEDPROFILEDEF'
        self.inverse={}
        self.OuterCurve=None #IfcCurve


    def load(self):
        """register inverses"""
        if not super(IFCARBITRARYCLOSEDPROFILEDEF,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCARBITRARYCLOSEDPROFILEDEF,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.OuterCurve= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCARBITRARYCLOSEDPROFILEDEF,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCARBITRARYCLOSEDPROFILEDEF,self).toString()       
        line += idToSPF(self.OuterCurve)+','

        return line

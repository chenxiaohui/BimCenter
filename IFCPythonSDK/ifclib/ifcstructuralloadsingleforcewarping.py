#!/usr/bin/python
#coding=utf-8
#Filename:IfcStructuralLoadSingleForceWarping.py
import log
import common
from ifcstructuralloadsingleforce import IFCSTRUCTURALLOADSINGLEFORCE

from utils import *

class IFCSTRUCTURALLOADSINGLEFORCEWARPING(IFCSTRUCTURALLOADSINGLEFORCE):
    """"""
    def __init__(self,id,arg):
        super(IFCSTRUCTURALLOADSINGLEFORCEWARPING,self).__init__(id,arg)
        self.type='IFCSTRUCTURALLOADSINGLEFORCEWARPING'
        self.inverse={}
        self.WarpingMoment=None #IfcWarpingMomentMeasure


    def load(self):
        """register inverses"""
        if not super(IFCSTRUCTURALLOADSINGLEFORCEWARPING,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSTRUCTURALLOADSINGLEFORCEWARPING,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.WarpingMoment= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSTRUCTURALLOADSINGLEFORCEWARPING,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCSTRUCTURALLOADSINGLEFORCEWARPING,self).toString()       
        line += integerToSPF(self.WarpingMoment)+','

        return line

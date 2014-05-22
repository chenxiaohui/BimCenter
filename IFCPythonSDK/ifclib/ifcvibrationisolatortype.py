#!/usr/bin/python
#coding=utf-8
#Filename:IfcVibrationIsolatorType.py
import log
import common
from ifcdiscreteaccessorytype import IFCDISCRETEACCESSORYTYPE

from utils import *

class IFCVIBRATIONISOLATORTYPE(IFCDISCRETEACCESSORYTYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCVIBRATIONISOLATORTYPE,self).__init__(id,arg)
        self.type='IFCVIBRATIONISOLATORTYPE'
        self.inverse={}
        self.PredefinedType=None #IfcVibrationIsolatorTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCVIBRATIONISOLATORTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCVIBRATIONISOLATORTYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCVIBRATIONISOLATORTYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCVIBRATIONISOLATORTYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line

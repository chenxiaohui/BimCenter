#!/usr/bin/python
#coding=utf-8
#Filename:IfcElectricMotorType.py
import log
import common
from ifcenergyconversiondevicetype import IFCENERGYCONVERSIONDEVICETYPE

from utils import *

class IFCELECTRICMOTORTYPE(IFCENERGYCONVERSIONDEVICETYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCELECTRICMOTORTYPE,self).__init__(id,arg)
        self.type='IFCELECTRICMOTORTYPE'
        self.inverse={}
        self.PredefinedType=None #IfcElectricMotorTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCELECTRICMOTORTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCELECTRICMOTORTYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCELECTRICMOTORTYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCELECTRICMOTORTYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line

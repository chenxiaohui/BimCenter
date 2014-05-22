#!/usr/bin/python
#coding=utf-8
#Filename:IfcAirToAirHeatRecoveryType.py
import log
import common
from ifcenergyconversiondevicetype import IFCENERGYCONVERSIONDEVICETYPE

from utils import *

class IFCAIRTOAIRHEATRECOVERYTYPE(IFCENERGYCONVERSIONDEVICETYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCAIRTOAIRHEATRECOVERYTYPE,self).__init__(id,arg)
        self.type='IFCAIRTOAIRHEATRECOVERYTYPE'
        self.inverse={}
        self.PredefinedType=None #IfcAirToAirHeatRecoveryTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCAIRTOAIRHEATRECOVERYTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCAIRTOAIRHEATRECOVERYTYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCAIRTOAIRHEATRECOVERYTYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCAIRTOAIRHEATRECOVERYTYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line

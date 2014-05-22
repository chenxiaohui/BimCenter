#!/usr/bin/python
#coding=utf-8
#Filename:IfcMotorConnectionType.py
import log
import common
from ifcenergyconversiondevicetype import IFCENERGYCONVERSIONDEVICETYPE

from utils import *

class IFCMOTORCONNECTIONTYPE(IFCENERGYCONVERSIONDEVICETYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCMOTORCONNECTIONTYPE,self).__init__(id,arg)
        self.type='IFCMOTORCONNECTIONTYPE'
        self.inverse={}
        self.PredefinedType=None #IfcMotorConnectionTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCMOTORCONNECTIONTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCMOTORCONNECTIONTYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCMOTORCONNECTIONTYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCMOTORCONNECTIONTYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line

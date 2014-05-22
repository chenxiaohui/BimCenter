#!/usr/bin/python
#coding=utf-8
#Filename:IfcAlarmType.py
import log
import common
from ifcdistributioncontrolelementtype import IFCDISTRIBUTIONCONTROLELEMENTTYPE

from utils import *

class IFCALARMTYPE(IFCDISTRIBUTIONCONTROLELEMENTTYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCALARMTYPE,self).__init__(id,arg)
        self.type='IFCALARMTYPE'
        self.inverse={}
        self.PredefinedType=None #IfcAlarmTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCALARMTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCALARMTYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCALARMTYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCALARMTYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line

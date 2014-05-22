#!/usr/bin/python
#coding=utf-8
#Filename:IfcUnitaryEquipmentType.py
import log
import common
from ifcenergyconversiondevicetype import IFCENERGYCONVERSIONDEVICETYPE

from utils import *

class IFCUNITARYEQUIPMENTTYPE(IFCENERGYCONVERSIONDEVICETYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCUNITARYEQUIPMENTTYPE,self).__init__(id,arg)
        self.type='IFCUNITARYEQUIPMENTTYPE'
        self.inverse={}
        self.PredefinedType=None #IfcUnitaryEquipmentTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCUNITARYEQUIPMENTTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCUNITARYEQUIPMENTTYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCUNITARYEQUIPMENTTYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCUNITARYEQUIPMENTTYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line

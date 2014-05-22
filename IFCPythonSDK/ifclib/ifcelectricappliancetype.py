#!/usr/bin/python
#coding=utf-8
#Filename:IfcElectricApplianceType.py
import log
import common
from ifcflowterminaltype import IFCFLOWTERMINALTYPE

from utils import *

class IFCELECTRICAPPLIANCETYPE(IFCFLOWTERMINALTYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCELECTRICAPPLIANCETYPE,self).__init__(id,arg)
        self.type='IFCELECTRICAPPLIANCETYPE'
        self.inverse={}
        self.PredefinedType=None #IfcElectricApplianceTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCELECTRICAPPLIANCETYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCELECTRICAPPLIANCETYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCELECTRICAPPLIANCETYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCELECTRICAPPLIANCETYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line

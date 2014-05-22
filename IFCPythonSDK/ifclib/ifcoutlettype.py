#!/usr/bin/python
#coding=utf-8
#Filename:IfcOutletType.py
import log
import common
from ifcflowterminaltype import IFCFLOWTERMINALTYPE

from utils import *

class IFCOUTLETTYPE(IFCFLOWTERMINALTYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCOUTLETTYPE,self).__init__(id,arg)
        self.type='IFCOUTLETTYPE'
        self.inverse={}
        self.PredefinedType=None #IfcOutletTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCOUTLETTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCOUTLETTYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCOUTLETTYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCOUTLETTYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line

#!/usr/bin/python
#coding=utf-8
#Filename:IfcControllerType.py
import log
import common
from ifcdistributioncontrolelementtype import IFCDISTRIBUTIONCONTROLELEMENTTYPE

from utils import *

class IFCCONTROLLERTYPE(IFCDISTRIBUTIONCONTROLELEMENTTYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCCONTROLLERTYPE,self).__init__(id,arg)
        self.type='IFCCONTROLLERTYPE'
        self.inverse={}
        self.PredefinedType=None #IfcControllerTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCCONTROLLERTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCONTROLLERTYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCONTROLLERTYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCCONTROLLERTYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line

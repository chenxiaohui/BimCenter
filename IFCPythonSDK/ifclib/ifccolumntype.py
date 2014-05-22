#!/usr/bin/python
#coding=utf-8
#Filename:IfcColumnType.py
import log
import common
from ifcbuildingelementtype import IFCBUILDINGELEMENTTYPE

from utils import *

class IFCCOLUMNTYPE(IFCBUILDINGELEMENTTYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCCOLUMNTYPE,self).__init__(id,arg)
        self.type='IFCCOLUMNTYPE'
        self.inverse={}
        self.PredefinedType=None #IfcColumnTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCCOLUMNTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCOLUMNTYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCOLUMNTYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCCOLUMNTYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line

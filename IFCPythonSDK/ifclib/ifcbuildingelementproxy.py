#!/usr/bin/python
#coding=utf-8
#Filename:IfcBuildingElementProxy.py
import log
import common
from ifcbuildingelement import IFCBUILDINGELEMENT

from utils import *

class IFCBUILDINGELEMENTPROXY(IFCBUILDINGELEMENT):
    """"""
    def __init__(self,id,arg):
        super(IFCBUILDINGELEMENTPROXY,self).__init__(id,arg)
        self.type='IFCBUILDINGELEMENTPROXY'
        self.inverse={}
        self.CompositionType=None #IfcElementCompositionEnum


    def load(self):
        """register inverses"""
        if not super(IFCBUILDINGELEMENTPROXY,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCBUILDINGELEMENTPROXY,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.CompositionType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCBUILDINGELEMENTPROXY,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCBUILDINGELEMENTPROXY,self).toString()       
        line += typerefToSPF(self.CompositionType)+','

        return line

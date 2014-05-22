#!/usr/bin/python
#coding=utf-8
#Filename:IfcRamp.py
import log
import common
from ifcbuildingelement import IFCBUILDINGELEMENT

from utils import *

class IFCRAMP(IFCBUILDINGELEMENT):
    """"""
    def __init__(self,id,arg):
        super(IFCRAMP,self).__init__(id,arg)
        self.type='IFCRAMP'
        self.inverse={}
        self.ShapeType=None #IfcRampTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCRAMP,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCRAMP,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ShapeType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCRAMP,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCRAMP,self).toString()       
        line += typerefToSPF(self.ShapeType)+','

        return line

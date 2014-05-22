#!/usr/bin/python
#coding=utf-8
#Filename:IfcRoof.py
import log
import common
from ifcbuildingelement import IFCBUILDINGELEMENT

from utils import *

class IFCROOF(IFCBUILDINGELEMENT):
    """"""
    def __init__(self,id,arg):
        super(IFCROOF,self).__init__(id,arg)
        self.type='IFCROOF'
        self.inverse={}
        self.ShapeType=None #IfcRoofTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCROOF,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCROOF,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ShapeType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCROOF,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCROOF,self).toString()       
        line += typerefToSPF(self.ShapeType)+','

        return line

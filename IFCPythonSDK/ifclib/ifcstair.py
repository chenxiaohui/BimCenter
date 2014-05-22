#!/usr/bin/python
#coding=utf-8
#Filename:IfcStair.py
import log
import common
from ifcbuildingelement import IFCBUILDINGELEMENT

from utils import *

class IFCSTAIR(IFCBUILDINGELEMENT):
    """"""
    def __init__(self,id,arg):
        super(IFCSTAIR,self).__init__(id,arg)
        self.type='IFCSTAIR'
        self.inverse={}
        self.ShapeType=None #IfcStairTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCSTAIR,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSTAIR,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ShapeType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSTAIR,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCSTAIR,self).toString()       
        line += typerefToSPF(self.ShapeType)+','

        return line

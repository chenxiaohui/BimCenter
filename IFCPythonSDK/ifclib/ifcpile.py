#!/usr/bin/python
#coding=utf-8
#Filename:IfcPile.py
import log
import common
from ifcbuildingelement import IFCBUILDINGELEMENT

from utils import *

class IFCPILE(IFCBUILDINGELEMENT):
    """"""
    def __init__(self,id,arg):
        super(IFCPILE,self).__init__(id,arg)
        self.type='IFCPILE'
        self.inverse={}
        self.PredefinedType=None #IfcPileTypeEnum
        self.ConstructionType=None #IfcPileConstructionEnum


    def load(self):
        """register inverses"""
        if not super(IFCPILE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCPILE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ConstructionType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCPILE,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCPILE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','
        line += typerefToSPF(self.ConstructionType)+','

        return line

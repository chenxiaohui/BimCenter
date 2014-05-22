#!/usr/bin/python
#coding=utf-8
#Filename:IfcOccupant.py
import log
import common
from ifcactor import IFCACTOR

from utils import *

class IFCOCCUPANT(IFCACTOR):
    """"""
    def __init__(self,id,arg):
        super(IFCOCCUPANT,self).__init__(id,arg)
        self.type='IFCOCCUPANT'
        self.inverse={}
        self.PredefinedType=None #IfcOccupantTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCOCCUPANT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCOCCUPANT,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCOCCUPANT,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCOCCUPANT,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line

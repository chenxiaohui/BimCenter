#!/usr/bin/python
#coding=utf-8
#Filename:IfcSpaceType.py
import log
import common
from ifcspatialstructureelementtype import IFCSPATIALSTRUCTUREELEMENTTYPE

from utils import *

class IFCSPACETYPE(IFCSPATIALSTRUCTUREELEMENTTYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCSPACETYPE,self).__init__(id,arg)
        self.type='IFCSPACETYPE'
        self.inverse={}
        self.PredefinedType=None #IfcSpaceTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCSPACETYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSPACETYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSPACETYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCSPACETYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line

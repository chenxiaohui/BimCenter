#!/usr/bin/python
#coding=utf-8
#Filename:IfcPolyLoop.py
import log
import common
from ifcloop import IFCLOOP

from utils import *

class IFCPOLYLOOP(IFCLOOP):
    """"""
    def __init__(self,id,arg):
        super(IFCPOLYLOOP,self).__init__(id,arg)
        self.type='IFCPOLYLOOP'
        self.inverse={}
        self.Polygon=None #LIST


    def load(self):
        """register inverses"""
        if not super(IFCPOLYLOOP,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCPOLYLOOP,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Polygon= getIdListParam(arg,spfToId)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCPOLYLOOP,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCPOLYLOOP,self).toString()       
        line += listParamToSPF(self.Polygon,idToSPF)+','

        return line

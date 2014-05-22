#!/usr/bin/python
#coding=utf-8
#Filename:IfcExtrudedAreaSolid.py
import log
import common
from ifcsweptareasolid import IFCSWEPTAREASOLID

from utils import *

class IFCEXTRUDEDAREASOLID(IFCSWEPTAREASOLID):
    """"""
    def __init__(self,id,arg):
        super(IFCEXTRUDEDAREASOLID,self).__init__(id,arg)
        self.type='IFCEXTRUDEDAREASOLID'
        self.inverse={}
        self.ExtrudedDirection=None #IfcDirection
        self.Depth=None #IfcPositiveLengthMeasure


    def load(self):
        """register inverses"""
        if not super(IFCEXTRUDEDAREASOLID,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCEXTRUDEDAREASOLID,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ExtrudedDirection= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Depth= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCEXTRUDEDAREASOLID,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCEXTRUDEDAREASOLID,self).toString()       
        line += idToSPF(self.ExtrudedDirection)+','
        line += integerToSPF(self.Depth)+','

        return line

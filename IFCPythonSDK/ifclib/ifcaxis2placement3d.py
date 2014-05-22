#!/usr/bin/python
#coding=utf-8
#Filename:IfcAxis2Placement3D.py
import log
import common
from ifcplacement import IFCPLACEMENT

from utils import *

class IFCAXIS2PLACEMENT3D(IFCPLACEMENT):
    """"""
    def __init__(self,id,arg):
        super(IFCAXIS2PLACEMENT3D,self).__init__(id,arg)
        self.type='IFCAXIS2PLACEMENT3D'
        self.inverse={}
        self.Axis=None #IfcDirection
        self.RefDirection=None #IfcDirection


    def load(self):
        """register inverses"""
        if not super(IFCAXIS2PLACEMENT3D,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCAXIS2PLACEMENT3D,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Axis= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RefDirection= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCAXIS2PLACEMENT3D,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCAXIS2PLACEMENT3D,self).toString()       
        line += idToSPF(self.Axis)+','
        line += idToSPF(self.RefDirection)+','

        return line

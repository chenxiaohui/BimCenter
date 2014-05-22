#!/usr/bin/python
#coding=utf-8
#Filename:IfcAxis2Placement2D.py
import log
import common
from ifcplacement import IFCPLACEMENT

from utils import *

class IFCAXIS2PLACEMENT2D(IFCPLACEMENT):
    """"""
    def __init__(self,id,arg):
        super(IFCAXIS2PLACEMENT2D,self).__init__(id,arg)
        self.type='IFCAXIS2PLACEMENT2D'
        self.inverse={}
        self.RefDirection=None #IfcDirection


    def load(self):
        """register inverses"""
        if not super(IFCAXIS2PLACEMENT2D,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCAXIS2PLACEMENT2D,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RefDirection= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCAXIS2PLACEMENT2D,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCAXIS2PLACEMENT2D,self).toString()       
        line += idToSPF(self.RefDirection)+','

        return line

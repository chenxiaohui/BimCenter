#!/usr/bin/python
#coding=utf-8
#Filename:IfcBoundaryNodeConditionWarping.py
import log
import common
from ifcboundarynodecondition import IFCBOUNDARYNODECONDITION

from utils import *

class IFCBOUNDARYNODECONDITIONWARPING(IFCBOUNDARYNODECONDITION):
    """"""
    def __init__(self,id,arg):
        super(IFCBOUNDARYNODECONDITIONWARPING,self).__init__(id,arg)
        self.type='IFCBOUNDARYNODECONDITIONWARPING'
        self.inverse={}
        self.WarpingStiffness=None #IfcWarpingMomentMeasure


    def load(self):
        """register inverses"""
        if not super(IFCBOUNDARYNODECONDITIONWARPING,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCBOUNDARYNODECONDITIONWARPING,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.WarpingStiffness= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCBOUNDARYNODECONDITIONWARPING,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCBOUNDARYNODECONDITIONWARPING,self).toString()       
        line += integerToSPF(self.WarpingStiffness)+','

        return line

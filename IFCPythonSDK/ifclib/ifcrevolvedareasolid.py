#!/usr/bin/python
#coding=utf-8
#Filename:IfcRevolvedAreaSolid.py
import log
import common
from ifcsweptareasolid import IFCSWEPTAREASOLID

from utils import *

class IFCREVOLVEDAREASOLID(IFCSWEPTAREASOLID):
    """"""
    def __init__(self,id,arg):
        super(IFCREVOLVEDAREASOLID,self).__init__(id,arg)
        self.type='IFCREVOLVEDAREASOLID'
        self.inverse={}
        self.Axis=None #IfcAxis1Placement
        self.Angle=None #IfcPlaneAngleMeasure


    def load(self):
        """register inverses"""
        if not super(IFCREVOLVEDAREASOLID,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCREVOLVEDAREASOLID,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Axis= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Angle= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCREVOLVEDAREASOLID,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCREVOLVEDAREASOLID,self).toString()       
        line += idToSPF(self.Axis)+','
        line += integerToSPF(self.Angle)+','

        return line

#!/usr/bin/python
#coding=utf-8
#Filename:IfcRightCircularCone.py
import log
import common
from ifccsgprimitive3d import IFCCSGPRIMITIVE3D

from utils import *

class IFCRIGHTCIRCULARCONE(IFCCSGPRIMITIVE3D):
    """"""
    def __init__(self,id,arg):
        super(IFCRIGHTCIRCULARCONE,self).__init__(id,arg)
        self.type='IFCRIGHTCIRCULARCONE'
        self.inverse={}
        self.Height=None #IfcPositiveLengthMeasure
        self.BottomRadius=None #IfcPositiveLengthMeasure


    def load(self):
        """register inverses"""
        if not super(IFCRIGHTCIRCULARCONE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCRIGHTCIRCULARCONE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Height= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.BottomRadius= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCRIGHTCIRCULARCONE,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCRIGHTCIRCULARCONE,self).toString()       
        line += integerToSPF(self.Height)+','
        line += integerToSPF(self.BottomRadius)+','

        return line

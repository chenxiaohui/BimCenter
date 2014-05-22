#!/usr/bin/python
#coding=utf-8
#Filename:IfcRightCircularCylinder.py
import log
import common
from ifccsgprimitive3d import IFCCSGPRIMITIVE3D

from utils import *

class IFCRIGHTCIRCULARCYLINDER(IFCCSGPRIMITIVE3D):
    """"""
    def __init__(self,id,arg):
        super(IFCRIGHTCIRCULARCYLINDER,self).__init__(id,arg)
        self.type='IFCRIGHTCIRCULARCYLINDER'
        self.inverse={}
        self.Height=None #IfcPositiveLengthMeasure
        self.Radius=None #IfcPositiveLengthMeasure


    def load(self):
        """register inverses"""
        if not super(IFCRIGHTCIRCULARCYLINDER,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCRIGHTCIRCULARCYLINDER,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Height= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Radius= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCRIGHTCIRCULARCYLINDER,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCRIGHTCIRCULARCYLINDER,self).toString()       
        line += integerToSPF(self.Height)+','
        line += integerToSPF(self.Radius)+','

        return line

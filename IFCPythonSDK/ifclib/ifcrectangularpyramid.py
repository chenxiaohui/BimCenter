#!/usr/bin/python
#coding=utf-8
#Filename:IfcRectangularPyramid.py
import log
import common
from ifccsgprimitive3d import IFCCSGPRIMITIVE3D

from utils import *

class IFCRECTANGULARPYRAMID(IFCCSGPRIMITIVE3D):
    """"""
    def __init__(self,id,arg):
        super(IFCRECTANGULARPYRAMID,self).__init__(id,arg)
        self.type='IFCRECTANGULARPYRAMID'
        self.inverse={}
        self.XLength=None #IfcPositiveLengthMeasure
        self.YLength=None #IfcPositiveLengthMeasure
        self.Height=None #IfcPositiveLengthMeasure


    def load(self):
        """register inverses"""
        if not super(IFCRECTANGULARPYRAMID,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCRECTANGULARPYRAMID,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.XLength= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.YLength= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Height= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCRECTANGULARPYRAMID,self).getAttrCount()+3

    def toString(self):
        """"""
        line=super(IFCRECTANGULARPYRAMID,self).toString()       
        line += integerToSPF(self.XLength)+','
        line += integerToSPF(self.YLength)+','
        line += integerToSPF(self.Height)+','

        return line

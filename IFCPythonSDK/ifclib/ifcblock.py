#!/usr/bin/python
#coding=utf-8
#Filename:IfcBlock.py
import log
import common
from ifccsgprimitive3d import IFCCSGPRIMITIVE3D

from utils import *

class IFCBLOCK(IFCCSGPRIMITIVE3D):
    """"""
    def __init__(self,id,arg):
        super(IFCBLOCK,self).__init__(id,arg)
        self.type='IFCBLOCK'
        self.inverse={}
        self.XLength=None #IfcPositiveLengthMeasure
        self.YLength=None #IfcPositiveLengthMeasure
        self.ZLength=None #IfcPositiveLengthMeasure


    def load(self):
        """register inverses"""
        if not super(IFCBLOCK,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCBLOCK,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.XLength= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.YLength= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ZLength= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCBLOCK,self).getAttrCount()+3

    def toString(self):
        """"""
        line=super(IFCBLOCK,self).toString()       
        line += integerToSPF(self.XLength)+','
        line += integerToSPF(self.YLength)+','
        line += integerToSPF(self.ZLength)+','

        return line

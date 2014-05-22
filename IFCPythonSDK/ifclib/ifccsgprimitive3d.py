#!/usr/bin/python
#coding=utf-8
#Filename:IfcCsgPrimitive3D.py
import log
import common
from ifcgeometricrepresentationitem import IFCGEOMETRICREPRESENTATIONITEM

from utils import *

class IFCCSGPRIMITIVE3D(IFCGEOMETRICREPRESENTATIONITEM):
    """"""
    def __init__(self,id,arg):
        super(IFCCSGPRIMITIVE3D,self).__init__(id,arg)
        self.type='IFCCSGPRIMITIVE3D'
        self.inverse={}
        self.Position=None #IfcAxis2Placement3D


    def load(self):
        """register inverses"""
        if not super(IFCCSGPRIMITIVE3D,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCSGPRIMITIVE3D,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Position= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCSGPRIMITIVE3D,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCCSGPRIMITIVE3D,self).toString()       
        line += idToSPF(self.Position)+','

        return line

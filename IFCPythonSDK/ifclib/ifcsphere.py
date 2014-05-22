#!/usr/bin/python
#coding=utf-8
#Filename:IfcSphere.py
import log
import common
from ifccsgprimitive3d import IFCCSGPRIMITIVE3D

from utils import *

class IFCSPHERE(IFCCSGPRIMITIVE3D):
    """"""
    def __init__(self,id,arg):
        super(IFCSPHERE,self).__init__(id,arg)
        self.type='IFCSPHERE'
        self.inverse={}
        self.Radius=None #IfcPositiveLengthMeasure


    def load(self):
        """register inverses"""
        if not super(IFCSPHERE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSPHERE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Radius= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSPHERE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCSPHERE,self).toString()       
        line += integerToSPF(self.Radius)+','

        return line

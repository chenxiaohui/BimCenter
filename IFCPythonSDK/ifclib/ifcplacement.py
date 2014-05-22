#!/usr/bin/python
#coding=utf-8
#Filename:IfcPlacement.py
import log
import common
from ifcgeometricrepresentationitem import IFCGEOMETRICREPRESENTATIONITEM

from utils import *

class IFCPLACEMENT(IFCGEOMETRICREPRESENTATIONITEM):
    """"""
    def __init__(self,id,arg):
        super(IFCPLACEMENT,self).__init__(id,arg)
        self.type='IFCPLACEMENT'
        self.inverse={}
        self.Location=None #IfcCartesianPoint


    def load(self):
        """register inverses"""
        if not super(IFCPLACEMENT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCPLACEMENT,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Location= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCPLACEMENT,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCPLACEMENT,self).toString()       
        line += idToSPF(self.Location)+','

        return line

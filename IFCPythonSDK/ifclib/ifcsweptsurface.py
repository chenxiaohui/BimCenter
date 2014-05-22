#!/usr/bin/python
#coding=utf-8
#Filename:IfcSweptSurface.py
import log
import common
from ifcsurface import IFCSURFACE

from utils import *

class IFCSWEPTSURFACE(IFCSURFACE):
    """"""
    def __init__(self,id,arg):
        super(IFCSWEPTSURFACE,self).__init__(id,arg)
        self.type='IFCSWEPTSURFACE'
        self.inverse={}
        self.SweptCurve=None #IfcProfileDef
        self.Position=None #IfcAxis2Placement3D


    def load(self):
        """register inverses"""
        if not super(IFCSWEPTSURFACE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSWEPTSURFACE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.SweptCurve= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Position= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSWEPTSURFACE,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCSWEPTSURFACE,self).toString()       
        line += idToSPF(self.SweptCurve)+','
        line += idToSPF(self.Position)+','

        return line

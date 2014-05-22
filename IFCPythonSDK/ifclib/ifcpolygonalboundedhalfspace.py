#!/usr/bin/python
#coding=utf-8
#Filename:IfcPolygonalBoundedHalfSpace.py
import log
import common
from ifchalfspacesolid import IFCHALFSPACESOLID

from utils import *

class IFCPOLYGONALBOUNDEDHALFSPACE(IFCHALFSPACESOLID):
    """"""
    def __init__(self,id,arg):
        super(IFCPOLYGONALBOUNDEDHALFSPACE,self).__init__(id,arg)
        self.type='IFCPOLYGONALBOUNDEDHALFSPACE'
        self.inverse={}
        self.Position=None #IfcAxis2Placement3D
        self.PolygonalBoundary=None #IfcBoundedCurve


    def load(self):
        """register inverses"""
        if not super(IFCPOLYGONALBOUNDEDHALFSPACE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCPOLYGONALBOUNDEDHALFSPACE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Position= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PolygonalBoundary= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCPOLYGONALBOUNDEDHALFSPACE,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCPOLYGONALBOUNDEDHALFSPACE,self).toString()       
        line += idToSPF(self.Position)+','
        line += idToSPF(self.PolygonalBoundary)+','

        return line

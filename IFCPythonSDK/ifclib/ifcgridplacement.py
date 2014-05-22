#!/usr/bin/python
#coding=utf-8
#Filename:IfcGridPlacement.py
import log
import common
from ifcobjectplacement import IFCOBJECTPLACEMENT

from utils import *

class IFCGRIDPLACEMENT(IFCOBJECTPLACEMENT):
    """"""
    def __init__(self,id,arg):
        super(IFCGRIDPLACEMENT,self).__init__(id,arg)
        self.type='IFCGRIDPLACEMENT'
        self.inverse={}
        self.PlacementLocation=None #IfcVirtualGridIntersection
        self.PlacementRefDirection=None #IfcVirtualGridIntersection


    def load(self):
        """register inverses"""
        if not super(IFCGRIDPLACEMENT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCGRIDPLACEMENT,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PlacementLocation= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PlacementRefDirection= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCGRIDPLACEMENT,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCGRIDPLACEMENT,self).toString()       
        line += idToSPF(self.PlacementLocation)+','
        line += idToSPF(self.PlacementRefDirection)+','

        return line

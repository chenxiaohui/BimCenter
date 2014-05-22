#!/usr/bin/python
#coding=utf-8
#Filename:IfcDoorPanelProperties.py
import log
import common
from ifcpropertysetdefinition import IFCPROPERTYSETDEFINITION

from utils import *

class IFCDOORPANELPROPERTIES(IFCPROPERTYSETDEFINITION):
    """"""
    def __init__(self,id,arg):
        super(IFCDOORPANELPROPERTIES,self).__init__(id,arg)
        self.type='IFCDOORPANELPROPERTIES'
        self.inverse={}
        self.PanelDepth=None #IfcPositiveLengthMeasure
        self.PanelOperation=None #IfcDoorPanelOperationEnum
        self.PanelWidth=None #IfcNormalisedRatioMeasure
        self.PanelPosition=None #IfcDoorPanelPositionEnum
        self.ShapeAspectStyle=None #IfcShapeAspect


    def load(self):
        """register inverses"""
        if not super(IFCDOORPANELPROPERTIES,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCDOORPANELPROPERTIES,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PanelDepth= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PanelOperation= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PanelWidth= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PanelPosition= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ShapeAspectStyle= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCDOORPANELPROPERTIES,self).getAttrCount()+5

    def toString(self):
        """"""
        line=super(IFCDOORPANELPROPERTIES,self).toString()       
        line += integerToSPF(self.PanelDepth)+','
        line += typerefToSPF(self.PanelOperation)+','
        line += integerToSPF(self.PanelWidth)+','
        line += typerefToSPF(self.PanelPosition)+','
        line += idToSPF(self.ShapeAspectStyle)+','

        return line

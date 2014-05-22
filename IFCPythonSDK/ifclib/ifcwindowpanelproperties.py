#!/usr/bin/python
#coding=utf-8
#Filename:IfcWindowPanelProperties.py
import log
import common
from ifcpropertysetdefinition import IFCPROPERTYSETDEFINITION

from utils import *

class IFCWINDOWPANELPROPERTIES(IFCPROPERTYSETDEFINITION):
    """"""
    def __init__(self,id,arg):
        super(IFCWINDOWPANELPROPERTIES,self).__init__(id,arg)
        self.type='IFCWINDOWPANELPROPERTIES'
        self.inverse={}
        self.OperationType=None #IfcWindowPanelOperationEnum
        self.PanelPosition=None #IfcWindowPanelPositionEnum
        self.FrameDepth=None #IfcPositiveLengthMeasure
        self.FrameThickness=None #IfcPositiveLengthMeasure
        self.ShapeAspectStyle=None #IfcShapeAspect


    def load(self):
        """register inverses"""
        if not super(IFCWINDOWPANELPROPERTIES,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCWINDOWPANELPROPERTIES,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.OperationType= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PanelPosition= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.FrameDepth= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.FrameThickness= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ShapeAspectStyle= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCWINDOWPANELPROPERTIES,self).getAttrCount()+5

    def toString(self):
        """"""
        line=super(IFCWINDOWPANELPROPERTIES,self).toString()       
        line += typerefToSPF(self.OperationType)+','
        line += typerefToSPF(self.PanelPosition)+','
        line += integerToSPF(self.FrameDepth)+','
        line += integerToSPF(self.FrameThickness)+','
        line += idToSPF(self.ShapeAspectStyle)+','

        return line

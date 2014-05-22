#!/usr/bin/python
#coding=utf-8
#Filename:IfcPermeableCoveringProperties.py
import log
import common
from ifcpropertysetdefinition import IFCPROPERTYSETDEFINITION

from utils import *

class IFCPERMEABLECOVERINGPROPERTIES(IFCPROPERTYSETDEFINITION):
    """"""
    def __init__(self,id,arg):
        super(IFCPERMEABLECOVERINGPROPERTIES,self).__init__(id,arg)
        self.type='IFCPERMEABLECOVERINGPROPERTIES'
        self.inverse={}
        self.OperationType=None #IfcPermeableCoveringOperationEnum
        self.PanelPosition=None #IfcWindowPanelPositionEnum
        self.FrameDepth=None #IfcPositiveLengthMeasure
        self.FrameThickness=None #IfcPositiveLengthMeasure
        self.ShapeAspectStyle=None #IfcShapeAspect


    def load(self):
        """register inverses"""
        if not super(IFCPERMEABLECOVERINGPROPERTIES,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCPERMEABLECOVERINGPROPERTIES,self).init():
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
        return super(IFCPERMEABLECOVERINGPROPERTIES,self).getAttrCount()+5

    def toString(self):
        """"""
        line=super(IFCPERMEABLECOVERINGPROPERTIES,self).toString()       
        line += typerefToSPF(self.OperationType)+','
        line += typerefToSPF(self.PanelPosition)+','
        line += integerToSPF(self.FrameDepth)+','
        line += integerToSPF(self.FrameThickness)+','
        line += idToSPF(self.ShapeAspectStyle)+','

        return line

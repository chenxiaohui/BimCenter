#!/usr/bin/python
#coding=utf-8
#Filename:IfcGridAxis.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCGRIDAXIS(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCGRIDAXIS,self).__init__(id,arg)
        self.type='IFCGRIDAXIS'
        self.inverse={}
        self.AxisTag=None #IfcLabel
        self.AxisCurve=None #IfcCurve
        self.SameSense=None #IfcBoolean
        self.inverse['PartOfW']=[] #inverse:SET of IfcGrid
        self.inverse['PartOfV']=[] #inverse:SET of IfcGrid
        self.inverse['PartOfU']=[] #inverse:SET of IfcGrid
        self.inverse['HasIntersections']=[] #inverse:SET of IfcVirtualGridIntersection


    def load(self):
        """register inverses"""
        if not super(IFCGRIDAXIS,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCGRIDAXIS,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.AxisTag= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.AxisCurve= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.SameSense= spfToLogical(arg)

        inverses = self.args.getInverses('IFCGRID', 'WAxes');
        if inverses:
            self.inverse['PartOfW']=inverses

        inverses = self.args.getInverses('IFCGRID', 'VAxes');
        if inverses:
            self.inverse['PartOfV']=inverses

        inverses = self.args.getInverses('IFCGRID', 'UAxes');
        if inverses:
            self.inverse['PartOfU']=inverses

        inverses = self.args.getInverses('IFCVIRTUALGRIDINTERSECTION', 'IntersectingAxes');
        if inverses:
            self.inverse['HasIntersections']=inverses

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCGRIDAXIS,self).getAttrCount()+3

    def toString(self):
        """"""
        line=super(IFCGRIDAXIS,self).toString()       
        line += strToSPF(self.AxisTag)+','
        line += idToSPF(self.AxisCurve)+','
        line += logicalToSPF(self.SameSense)+','

        return line

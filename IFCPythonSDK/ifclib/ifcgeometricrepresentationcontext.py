#!/usr/bin/python
#coding=utf-8
#Filename:IfcGeometricRepresentationContext.py
import log
import common
from ifcrepresentationcontext import IFCREPRESENTATIONCONTEXT

from utils import *

class IFCGEOMETRICREPRESENTATIONCONTEXT(IFCREPRESENTATIONCONTEXT):
    """"""
    def __init__(self,id,arg):
        super(IFCGEOMETRICREPRESENTATIONCONTEXT,self).__init__(id,arg)
        self.type='IFCGEOMETRICREPRESENTATIONCONTEXT'
        self.inverse={}
        self.CoordinateSpaceDimension=None #IfcDimensionCount
        self.Precision=None #REAL
        self.WorldCoordinateSystem=None #IfcAxis2Placement
        self.TrueNorth=None #IfcDirection
        self.inverse['HasSubContexts']=[] #inverse:SET of IfcGeometricRepresentationSubContext


    def load(self):
        """register inverses"""
        if not super(IFCGEOMETRICREPRESENTATIONCONTEXT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCGEOMETRICREPRESENTATIONCONTEXT,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.CoordinateSpaceDimension= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Precision= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.WorldCoordinateSystem= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.TrueNorth= spfToId(arg)

        inverses = self.args.getInverses('IFCGEOMETRICREPRESENTATIONSUBCONTEXT', 'ParentContext');
        if inverses:
            self.inverse['HasSubContexts']=inverses

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCGEOMETRICREPRESENTATIONCONTEXT,self).getAttrCount()+4

    def toString(self):
        """"""
        line=super(IFCGEOMETRICREPRESENTATIONCONTEXT,self).toString()       
        line += integerToSPF(self.CoordinateSpaceDimension)+','
        line += integerToSPF(self.Precision)+','
        line += typerefToSPF(self.WorldCoordinateSystem)+','
        line += idToSPF(self.TrueNorth)+','

        return line

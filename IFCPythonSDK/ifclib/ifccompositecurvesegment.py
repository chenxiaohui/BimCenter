#!/usr/bin/python
#coding=utf-8
#Filename:IfcCompositeCurveSegment.py
import log
import common
from ifcgeometricrepresentationitem import IFCGEOMETRICREPRESENTATIONITEM

from utils import *

class IFCCOMPOSITECURVESEGMENT(IFCGEOMETRICREPRESENTATIONITEM):
    """"""
    def __init__(self,id,arg):
        super(IFCCOMPOSITECURVESEGMENT,self).__init__(id,arg)
        self.type='IFCCOMPOSITECURVESEGMENT'
        self.inverse={}
        self.Transition=None #IfcTransitionCode
        self.SameSense=None #BOOLEAN
        self.ParentCurve=None #IfcCurve
        self.inverse['UsingCurves']=[] #inverse:SET of IfcCompositeCurve


    def load(self):
        """register inverses"""
        if not super(IFCCOMPOSITECURVESEGMENT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCOMPOSITECURVESEGMENT,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Transition= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.SameSense= spfToLogical(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ParentCurve= spfToId(arg)

        inverses = self.args.getInverses('IFCCOMPOSITECURVE', 'Segments');
        if inverses:
            self.inverse['UsingCurves']=inverses

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCOMPOSITECURVESEGMENT,self).getAttrCount()+3

    def toString(self):
        """"""
        line=super(IFCCOMPOSITECURVESEGMENT,self).toString()       
        line += typerefToSPF(self.Transition)+','
        line += logicalToSPF(self.SameSense)+','
        line += idToSPF(self.ParentCurve)+','

        return line

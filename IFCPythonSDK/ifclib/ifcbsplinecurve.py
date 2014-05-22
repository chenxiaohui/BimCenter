#!/usr/bin/python
#coding=utf-8
#Filename:IfcBSplineCurve.py
import log
import common
from ifcboundedcurve import IFCBOUNDEDCURVE

from utils import *

class IFCBSPLINECURVE(IFCBOUNDEDCURVE):
    """"""
    def __init__(self,id,arg):
        super(IFCBSPLINECURVE,self).__init__(id,arg)
        self.type='IFCBSPLINECURVE'
        self.inverse={}
        self.Degree=None #INTEGER
        self.ControlPointsList=None #LIST
        self.CurveForm=None #IfcBSplineCurveForm
        self.ClosedCurve=None #LOGICAL
        self.SelfIntersect=None #LOGICAL


    def load(self):
        """register inverses"""
        if not super(IFCBSPLINECURVE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCBSPLINECURVE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Degree= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ControlPointsList= getIdListParam(arg,spfToId)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.CurveForm= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ClosedCurve= spfToLogical(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.SelfIntersect= spfToLogical(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCBSPLINECURVE,self).getAttrCount()+5

    def toString(self):
        """"""
        line=super(IFCBSPLINECURVE,self).toString()       
        line += integerToSPF(self.Degree)+','
        line += listParamToSPF(self.ControlPointsList,idToSPF)+','
        line += typerefToSPF(self.CurveForm)+','
        line += logicalToSPF(self.ClosedCurve)+','
        line += logicalToSPF(self.SelfIntersect)+','

        return line

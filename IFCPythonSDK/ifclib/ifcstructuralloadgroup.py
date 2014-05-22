#!/usr/bin/python
#coding=utf-8
#Filename:IfcStructuralLoadGroup.py
import log
import common
from ifcgroup import IFCGROUP

from utils import *

class IFCSTRUCTURALLOADGROUP(IFCGROUP):
    """"""
    def __init__(self,id,arg):
        super(IFCSTRUCTURALLOADGROUP,self).__init__(id,arg)
        self.type='IFCSTRUCTURALLOADGROUP'
        self.inverse={}
        self.PredefinedType=None #IfcLoadGroupTypeEnum
        self.ActionType=None #IfcActionTypeEnum
        self.ActionSource=None #IfcActionSourceTypeEnum
        self.Coefficient=None #IfcRatioMeasure
        self.Purpose=None #IfcLabel
        self.inverse['LoadGroupFor']=[] #inverse:SET of IfcStructuralAnalysisModel
        self.inverse['SourceOfResultGroup']=[] #inverse:SET of IfcStructuralResultGroup


    def load(self):
        """register inverses"""
        if not super(IFCSTRUCTURALLOADGROUP,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSTRUCTURALLOADGROUP,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ActionType= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ActionSource= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Coefficient= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Purpose= fromSPF(arg)

        inverses = self.args.getInverses('IFCSTRUCTURALANALYSISMODEL', 'LoadedBy');
        if inverses:
            self.inverse['LoadGroupFor']=inverses

        inverses = self.args.getInverses('IFCSTRUCTURALRESULTGROUP', 'ResultForLoadGroup');
        if inverses:
            self.inverse['SourceOfResultGroup']=inverses

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSTRUCTURALLOADGROUP,self).getAttrCount()+5

    def toString(self):
        """"""
        line=super(IFCSTRUCTURALLOADGROUP,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','
        line += typerefToSPF(self.ActionType)+','
        line += typerefToSPF(self.ActionSource)+','
        line += integerToSPF(self.Coefficient)+','
        line += strToSPF(self.Purpose)+','

        return line

#!/usr/bin/python
#coding=utf-8
#Filename:IfcRelConnectsStructuralMember.py
import log
import common
from ifcrelconnects import IFCRELCONNECTS

from utils import *

class IFCRELCONNECTSSTRUCTURALMEMBER(IFCRELCONNECTS):
    """"""
    def __init__(self,id,arg):
        super(IFCRELCONNECTSSTRUCTURALMEMBER,self).__init__(id,arg)
        self.type='IFCRELCONNECTSSTRUCTURALMEMBER'
        self.inverse={}
        self.RelatingStructuralMember=None #IfcStructuralMember
        self.RelatedStructuralConnection=None #IfcStructuralConnection
        self.AppliedCondition=None #IfcBoundaryCondition
        self.AdditionalConditions=None #IfcStructuralConnectionCondition
        self.SupportedLength=None #IfcLengthMeasure
        self.ConditionCoordinateSystem=None #IfcAxis2Placement3D


    def load(self):
        """register inverses"""
        if not super(IFCRELCONNECTSSTRUCTURALMEMBER,self).load():
            return False
        idx=super(IFCRELCONNECTSSTRUCTURALMEMBER,self).getAttrCount()
        if self.args.argc()<=idx+0:
            log.error("Inverse links : Error during reading parameter 0 of IfcRelConnectsStructuralMember, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+0])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 0 of IfcRelConnectsStructuralMember, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCRELCONNECTSSTRUCTURALMEMBER','RelatingStructuralMember',self.lid)
        if self.args.argc()<=idx+1:
            log.error("Inverse links : Error during reading parameter 1 of IfcRelConnectsStructuralMember, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+1])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 1 of IfcRelConnectsStructuralMember, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCRELCONNECTSSTRUCTURALMEMBER','RelatedStructuralConnection',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCRELCONNECTSSTRUCTURALMEMBER,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatingStructuralMember= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatedStructuralConnection= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.AppliedCondition= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.AdditionalConditions= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.SupportedLength= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ConditionCoordinateSystem= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCRELCONNECTSSTRUCTURALMEMBER,self).getAttrCount()+6

    def toString(self):
        """"""
        line=super(IFCRELCONNECTSSTRUCTURALMEMBER,self).toString()       
        line += idToSPF(self.RelatingStructuralMember)+','
        line += idToSPF(self.RelatedStructuralConnection)+','
        line += idToSPF(self.AppliedCondition)+','
        line += idToSPF(self.AdditionalConditions)+','
        line += integerToSPF(self.SupportedLength)+','
        line += idToSPF(self.ConditionCoordinateSystem)+','

        return line

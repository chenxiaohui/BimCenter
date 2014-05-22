#!/usr/bin/python
#coding=utf-8
#Filename:IfcRelReferencedInSpatialStructure.py
import log
import common
from ifcrelconnects import IFCRELCONNECTS

from utils import *

class IFCRELREFERENCEDINSPATIALSTRUCTURE(IFCRELCONNECTS):
    """"""
    def __init__(self,id,arg):
        super(IFCRELREFERENCEDINSPATIALSTRUCTURE,self).__init__(id,arg)
        self.type='IFCRELREFERENCEDINSPATIALSTRUCTURE'
        self.inverse={}
        self.RelatedElements=None #SET
        self.RelatingStructure=None #IfcSpatialStructureElement


    def load(self):
        """register inverses"""
        if not super(IFCRELREFERENCEDINSPATIALSTRUCTURE,self).load():
            return False
        idx=super(IFCRELREFERENCEDINSPATIALSTRUCTURE,self).getAttrCount()
        if self.args.argc()<=idx+0:
            log.error("Inverse links : Error during reading parameter 0 of IfcRelReferencedInSpatialStructure, line %d"%common.counter)
            return False

        currentRefList=getIdListParam(self.args.argv[idx+0])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 0 of IfcRelReferencedInSpatialStructure, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCRELREFERENCEDINSPATIALSTRUCTURE','RelatedElements',self.lid)
        if self.args.argc()<=idx+1:
            log.error("Inverse links : Error during reading parameter 1 of IfcRelReferencedInSpatialStructure, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+1])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 1 of IfcRelReferencedInSpatialStructure, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCRELREFERENCEDINSPATIALSTRUCTURE','RelatingStructure',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCRELREFERENCEDINSPATIALSTRUCTURE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatedElements= getIdListParam(arg,spfToId)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatingStructure= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCRELREFERENCEDINSPATIALSTRUCTURE,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCRELREFERENCEDINSPATIALSTRUCTURE,self).toString()       
        line += listParamToSPF(self.RelatedElements,idToSPF)+','
        line += idToSPF(self.RelatingStructure)+','

        return line

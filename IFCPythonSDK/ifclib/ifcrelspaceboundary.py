#!/usr/bin/python
#coding=utf-8
#Filename:IfcRelSpaceBoundary.py
import log
import common
from ifcrelconnects import IFCRELCONNECTS

from utils import *

class IFCRELSPACEBOUNDARY(IFCRELCONNECTS):
    """"""
    def __init__(self,id,arg):
        super(IFCRELSPACEBOUNDARY,self).__init__(id,arg)
        self.type='IFCRELSPACEBOUNDARY'
        self.inverse={}
        self.RelatingSpace=None #IfcSpace
        self.RelatedBuildingElement=None #IfcElement
        self.ConnectionGeometry=None #IfcConnectionGeometry
        self.PhysicalOrVirtualBoundary=None #IfcPhysicalOrVirtualEnum
        self.InternalOrExternalBoundary=None #IfcInternalOrExternalEnum


    def load(self):
        """register inverses"""
        if not super(IFCRELSPACEBOUNDARY,self).load():
            return False
        idx=super(IFCRELSPACEBOUNDARY,self).getAttrCount()
        if self.args.argc()<=idx+0:
            log.error("Inverse links : Error during reading parameter 0 of IfcRelSpaceBoundary, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+0])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 0 of IfcRelSpaceBoundary, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCRELSPACEBOUNDARY','RelatingSpace',self.lid)
        if self.args.argc()<=idx+1:
            log.error("Inverse links : Error during reading parameter 1 of IfcRelSpaceBoundary, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+1])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 1 of IfcRelSpaceBoundary, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCRELSPACEBOUNDARY','RelatedBuildingElement',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCRELSPACEBOUNDARY,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatingSpace= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatedBuildingElement= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ConnectionGeometry= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PhysicalOrVirtualBoundary= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.InternalOrExternalBoundary= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCRELSPACEBOUNDARY,self).getAttrCount()+5

    def toString(self):
        """"""
        line=super(IFCRELSPACEBOUNDARY,self).toString()       
        line += idToSPF(self.RelatingSpace)+','
        line += idToSPF(self.RelatedBuildingElement)+','
        line += idToSPF(self.ConnectionGeometry)+','
        line += typerefToSPF(self.PhysicalOrVirtualBoundary)+','
        line += typerefToSPF(self.InternalOrExternalBoundary)+','

        return line

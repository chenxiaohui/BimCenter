#!/usr/bin/python
#coding=utf-8
#Filename:IfcRelCoversBldgElements.py
import log
import common
from ifcrelconnects import IFCRELCONNECTS

from utils import *

class IFCRELCOVERSBLDGELEMENTS(IFCRELCONNECTS):
    """"""
    def __init__(self,id,arg):
        super(IFCRELCOVERSBLDGELEMENTS,self).__init__(id,arg)
        self.type='IFCRELCOVERSBLDGELEMENTS'
        self.inverse={}
        self.RelatingBuildingElement=None #IfcElement
        self.RelatedCoverings=None #SET


    def load(self):
        """register inverses"""
        if not super(IFCRELCOVERSBLDGELEMENTS,self).load():
            return False
        idx=super(IFCRELCOVERSBLDGELEMENTS,self).getAttrCount()
        if self.args.argc()<=idx+0:
            log.error("Inverse links : Error during reading parameter 0 of IfcRelCoversBldgElements, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+0])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 0 of IfcRelCoversBldgElements, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCRELCOVERSBLDGELEMENTS','RelatingBuildingElement',self.lid)
        if self.args.argc()<=idx+1:
            log.error("Inverse links : Error during reading parameter 1 of IfcRelCoversBldgElements, line %d"%common.counter)
            return False

        currentRefList=getIdListParam(self.args.argv[idx+1])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 1 of IfcRelCoversBldgElements, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCRELCOVERSBLDGELEMENTS','RelatedCoverings',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCRELCOVERSBLDGELEMENTS,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatingBuildingElement= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatedCoverings= getIdListParam(arg,spfToId)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCRELCOVERSBLDGELEMENTS,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCRELCOVERSBLDGELEMENTS,self).toString()       
        line += idToSPF(self.RelatingBuildingElement)+','
        line += listParamToSPF(self.RelatedCoverings,idToSPF)+','

        return line

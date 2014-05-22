#!/usr/bin/python
#coding=utf-8
#Filename:IfcRelCoversSpaces.py
import log
import common
from ifcrelconnects import IFCRELCONNECTS

from utils import *

class IFCRELCOVERSSPACES(IFCRELCONNECTS):
    """"""
    def __init__(self,id,arg):
        super(IFCRELCOVERSSPACES,self).__init__(id,arg)
        self.type='IFCRELCOVERSSPACES'
        self.inverse={}
        self.RelatedSpace=None #IfcSpace
        self.RelatedCoverings=None #SET


    def load(self):
        """register inverses"""
        if not super(IFCRELCOVERSSPACES,self).load():
            return False
        idx=super(IFCRELCOVERSSPACES,self).getAttrCount()
        if self.args.argc()<=idx+0:
            log.error("Inverse links : Error during reading parameter 0 of IfcRelCoversSpaces, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+0])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 0 of IfcRelCoversSpaces, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCRELCOVERSSPACES','RelatedSpace',self.lid)
        if self.args.argc()<=idx+1:
            log.error("Inverse links : Error during reading parameter 1 of IfcRelCoversSpaces, line %d"%common.counter)
            return False

        currentRefList=getIdListParam(self.args.argv[idx+1])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 1 of IfcRelCoversSpaces, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCRELCOVERSSPACES','RelatedCoverings',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCRELCOVERSSPACES,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatedSpace= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatedCoverings= getIdListParam(arg,spfToId)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCRELCOVERSSPACES,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCRELCOVERSSPACES,self).toString()       
        line += idToSPF(self.RelatedSpace)+','
        line += listParamToSPF(self.RelatedCoverings,idToSPF)+','

        return line

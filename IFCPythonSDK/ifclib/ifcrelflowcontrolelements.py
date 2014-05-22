#!/usr/bin/python
#coding=utf-8
#Filename:IfcRelFlowControlElements.py
import log
import common
from ifcrelconnects import IFCRELCONNECTS

from utils import *

class IFCRELFLOWCONTROLELEMENTS(IFCRELCONNECTS):
    """"""
    def __init__(self,id,arg):
        super(IFCRELFLOWCONTROLELEMENTS,self).__init__(id,arg)
        self.type='IFCRELFLOWCONTROLELEMENTS'
        self.inverse={}
        self.RelatedControlElements=None #SET
        self.RelatingFlowElement=None #IfcDistributionFlowElement


    def load(self):
        """register inverses"""
        if not super(IFCRELFLOWCONTROLELEMENTS,self).load():
            return False
        idx=super(IFCRELFLOWCONTROLELEMENTS,self).getAttrCount()
        if self.args.argc()<=idx+0:
            log.error("Inverse links : Error during reading parameter 0 of IfcRelFlowControlElements, line %d"%common.counter)
            return False

        currentRefList=getIdListParam(self.args.argv[idx+0])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 0 of IfcRelFlowControlElements, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCRELFLOWCONTROLELEMENTS','RelatedControlElements',self.lid)
        if self.args.argc()<=idx+1:
            log.error("Inverse links : Error during reading parameter 1 of IfcRelFlowControlElements, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+1])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 1 of IfcRelFlowControlElements, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCRELFLOWCONTROLELEMENTS','RelatingFlowElement',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCRELFLOWCONTROLELEMENTS,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatedControlElements= getIdListParam(arg,spfToId)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatingFlowElement= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCRELFLOWCONTROLELEMENTS,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCRELFLOWCONTROLELEMENTS,self).toString()       
        line += listParamToSPF(self.RelatedControlElements,idToSPF)+','
        line += idToSPF(self.RelatingFlowElement)+','

        return line

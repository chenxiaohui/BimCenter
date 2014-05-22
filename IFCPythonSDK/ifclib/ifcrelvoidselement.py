#!/usr/bin/python
#coding=utf-8
#Filename:IfcRelVoidsElement.py
import log
import common
from ifcrelconnects import IFCRELCONNECTS

from utils import *

class IFCRELVOIDSELEMENT(IFCRELCONNECTS):
    """"""
    def __init__(self,id,arg):
        super(IFCRELVOIDSELEMENT,self).__init__(id,arg)
        self.type='IFCRELVOIDSELEMENT'
        self.inverse={}
        self.RelatingBuildingElement=None #IfcElement
        self.RelatedOpeningElement=None #IfcFeatureElementSubtraction


    def load(self):
        """register inverses"""
        if not super(IFCRELVOIDSELEMENT,self).load():
            return False
        idx=super(IFCRELVOIDSELEMENT,self).getAttrCount()
        if self.args.argc()<=idx+0:
            log.error("Inverse links : Error during reading parameter 0 of IfcRelVoidsElement, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+0])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 0 of IfcRelVoidsElement, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCRELVOIDSELEMENT','RelatingBuildingElement',self.lid)
        if self.args.argc()<=idx+1:
            log.error("Inverse links : Error during reading parameter 1 of IfcRelVoidsElement, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+1])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 1 of IfcRelVoidsElement, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCRELVOIDSELEMENT','RelatedOpeningElement',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCRELVOIDSELEMENT,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatingBuildingElement= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatedOpeningElement= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCRELVOIDSELEMENT,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCRELVOIDSELEMENT,self).toString()       
        line += idToSPF(self.RelatingBuildingElement)+','
        line += idToSPF(self.RelatedOpeningElement)+','

        return line

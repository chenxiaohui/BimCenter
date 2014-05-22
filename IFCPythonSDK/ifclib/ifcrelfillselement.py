#!/usr/bin/python
#coding=utf-8
#Filename:IfcRelFillsElement.py
import log
import common
from ifcrelconnects import IFCRELCONNECTS

from utils import *

class IFCRELFILLSELEMENT(IFCRELCONNECTS):
    """"""
    def __init__(self,id,arg):
        super(IFCRELFILLSELEMENT,self).__init__(id,arg)
        self.type='IFCRELFILLSELEMENT'
        self.inverse={}
        self.RelatingOpeningElement=None #IfcOpeningElement
        self.RelatedBuildingElement=None #IfcElement


    def load(self):
        """register inverses"""
        if not super(IFCRELFILLSELEMENT,self).load():
            return False
        idx=super(IFCRELFILLSELEMENT,self).getAttrCount()
        if self.args.argc()<=idx+0:
            log.error("Inverse links : Error during reading parameter 0 of IfcRelFillsElement, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+0])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 0 of IfcRelFillsElement, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCRELFILLSELEMENT','RelatingOpeningElement',self.lid)
        if self.args.argc()<=idx+1:
            log.error("Inverse links : Error during reading parameter 1 of IfcRelFillsElement, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+1])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 1 of IfcRelFillsElement, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCRELFILLSELEMENT','RelatedBuildingElement',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCRELFILLSELEMENT,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatingOpeningElement= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatedBuildingElement= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCRELFILLSELEMENT,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCRELFILLSELEMENT,self).toString()       
        line += idToSPF(self.RelatingOpeningElement)+','
        line += idToSPF(self.RelatedBuildingElement)+','

        return line

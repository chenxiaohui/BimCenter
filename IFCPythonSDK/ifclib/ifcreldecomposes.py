#!/usr/bin/python
#coding=utf-8
#Filename:IfcRelDecomposes.py
import log
import common
from ifcrelationship import IFCRELATIONSHIP

from utils import *

class IFCRELDECOMPOSES(IFCRELATIONSHIP):
    """"""
    def __init__(self,id,arg):
        super(IFCRELDECOMPOSES,self).__init__(id,arg)
        self.type='IFCRELDECOMPOSES'
        self.inverse={}
        self.RelatingObject=None #IfcObjectDefinition
        self.RelatedObjects=None #SET


    def load(self):
        """register inverses"""
        if not super(IFCRELDECOMPOSES,self).load():
            return False
        idx=super(IFCRELDECOMPOSES,self).getAttrCount()
        if self.args.argc()<=idx+0:
            log.error("Inverse links : Error during reading parameter 0 of IfcRelDecomposes, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+0])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 0 of IfcRelDecomposes, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCRELDECOMPOSES','RelatingObject',self.lid)
        if self.args.argc()<=idx+1:
            log.error("Inverse links : Error during reading parameter 1 of IfcRelDecomposes, line %d"%common.counter)
            return False

        currentRefList=getIdListParam(self.args.argv[idx+1])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 1 of IfcRelDecomposes, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCRELDECOMPOSES','RelatedObjects',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCRELDECOMPOSES,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatingObject= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatedObjects= getIdListParam(arg,spfToId)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCRELDECOMPOSES,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCRELDECOMPOSES,self).toString()       
        line += idToSPF(self.RelatingObject)+','
        line += listParamToSPF(self.RelatedObjects,idToSPF)+','

        return line

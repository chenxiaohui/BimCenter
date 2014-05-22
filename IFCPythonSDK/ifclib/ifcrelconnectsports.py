#!/usr/bin/python
#coding=utf-8
#Filename:IfcRelConnectsPorts.py
import log
import common
from ifcrelconnects import IFCRELCONNECTS

from utils import *

class IFCRELCONNECTSPORTS(IFCRELCONNECTS):
    """"""
    def __init__(self,id,arg):
        super(IFCRELCONNECTSPORTS,self).__init__(id,arg)
        self.type='IFCRELCONNECTSPORTS'
        self.inverse={}
        self.RelatingPort=None #IfcPort
        self.RelatedPort=None #IfcPort
        self.RealizingElement=None #IfcElement


    def load(self):
        """register inverses"""
        if not super(IFCRELCONNECTSPORTS,self).load():
            return False
        idx=super(IFCRELCONNECTSPORTS,self).getAttrCount()
        if self.args.argc()<=idx+0:
            log.error("Inverse links : Error during reading parameter 0 of IfcRelConnectsPorts, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+0])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 0 of IfcRelConnectsPorts, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCRELCONNECTSPORTS','RelatingPort',self.lid)
        if self.args.argc()<=idx+1:
            log.error("Inverse links : Error during reading parameter 1 of IfcRelConnectsPorts, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+1])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 1 of IfcRelConnectsPorts, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCRELCONNECTSPORTS','RelatedPort',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCRELCONNECTSPORTS,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatingPort= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatedPort= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RealizingElement= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCRELCONNECTSPORTS,self).getAttrCount()+3

    def toString(self):
        """"""
        line=super(IFCRELCONNECTSPORTS,self).toString()       
        line += idToSPF(self.RelatingPort)+','
        line += idToSPF(self.RelatedPort)+','
        line += idToSPF(self.RealizingElement)+','

        return line

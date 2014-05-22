#!/usr/bin/python
#coding=utf-8
#Filename:IfcRelConnectsElements.py
import log
import common
from ifcrelconnects import IFCRELCONNECTS

from utils import *

class IFCRELCONNECTSELEMENTS(IFCRELCONNECTS):
    """"""
    def __init__(self,id,arg):
        super(IFCRELCONNECTSELEMENTS,self).__init__(id,arg)
        self.type='IFCRELCONNECTSELEMENTS'
        self.inverse={}
        self.ConnectionGeometry=None #IfcConnectionGeometry
        self.RelatingElement=None #IfcElement
        self.RelatedElement=None #IfcElement


    def load(self):
        """register inverses"""
        if not super(IFCRELCONNECTSELEMENTS,self).load():
            return False
        idx=super(IFCRELCONNECTSELEMENTS,self).getAttrCount()
        if self.args.argc()<=idx+1:
            log.error("Inverse links : Error during reading parameter 1 of IfcRelConnectsElements, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+1])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 1 of IfcRelConnectsElements, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCRELCONNECTSELEMENTS','RelatingElement',self.lid)
        if self.args.argc()<=idx+2:
            log.error("Inverse links : Error during reading parameter 2 of IfcRelConnectsElements, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+2])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 2 of IfcRelConnectsElements, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCRELCONNECTSELEMENTS','RelatedElement',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCRELCONNECTSELEMENTS,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ConnectionGeometry= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatingElement= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatedElement= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCRELCONNECTSELEMENTS,self).getAttrCount()+3

    def toString(self):
        """"""
        line=super(IFCRELCONNECTSELEMENTS,self).toString()       
        line += idToSPF(self.ConnectionGeometry)+','
        line += idToSPF(self.RelatingElement)+','
        line += idToSPF(self.RelatedElement)+','

        return line

#!/usr/bin/python
#coding=utf-8
#Filename:IfcRelConnectsWithRealizingElements.py
import log
import common
from ifcrelconnectselements import IFCRELCONNECTSELEMENTS

from utils import *

class IFCRELCONNECTSWITHREALIZINGELEMENTS(IFCRELCONNECTSELEMENTS):
    """"""
    def __init__(self,id,arg):
        super(IFCRELCONNECTSWITHREALIZINGELEMENTS,self).__init__(id,arg)
        self.type='IFCRELCONNECTSWITHREALIZINGELEMENTS'
        self.inverse={}
        self.RealizingElements=None #SET
        self.ConnectionType=None #IfcLabel


    def load(self):
        """register inverses"""
        if not super(IFCRELCONNECTSWITHREALIZINGELEMENTS,self).load():
            return False
        idx=super(IFCRELCONNECTSWITHREALIZINGELEMENTS,self).getAttrCount()
        if self.args.argc()<=idx+0:
            log.error("Inverse links : Error during reading parameter 0 of IfcRelConnectsWithRealizingElements, line %d"%common.counter)
            return False

        currentRefList=getIdListParam(self.args.argv[idx+0])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 0 of IfcRelConnectsWithRealizingElements, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCRELCONNECTSWITHREALIZINGELEMENTS','RealizingElements',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCRELCONNECTSWITHREALIZINGELEMENTS,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RealizingElements= getIdListParam(arg,spfToId)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ConnectionType= fromSPF(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCRELCONNECTSWITHREALIZINGELEMENTS,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCRELCONNECTSWITHREALIZINGELEMENTS,self).toString()       
        line += listParamToSPF(self.RealizingElements,idToSPF)+','
        line += strToSPF(self.ConnectionType)+','

        return line

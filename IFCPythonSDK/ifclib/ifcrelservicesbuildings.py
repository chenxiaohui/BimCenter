#!/usr/bin/python
#coding=utf-8
#Filename:IfcRelServicesBuildings.py
import log
import common
from ifcrelconnects import IFCRELCONNECTS

from utils import *

class IFCRELSERVICESBUILDINGS(IFCRELCONNECTS):
    """"""
    def __init__(self,id,arg):
        super(IFCRELSERVICESBUILDINGS,self).__init__(id,arg)
        self.type='IFCRELSERVICESBUILDINGS'
        self.inverse={}
        self.RelatingSystem=None #IfcSystem
        self.RelatedBuildings=None #SET


    def load(self):
        """register inverses"""
        if not super(IFCRELSERVICESBUILDINGS,self).load():
            return False
        idx=super(IFCRELSERVICESBUILDINGS,self).getAttrCount()
        if self.args.argc()<=idx+0:
            log.error("Inverse links : Error during reading parameter 0 of IfcRelServicesBuildings, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+0])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 0 of IfcRelServicesBuildings, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCRELSERVICESBUILDINGS','RelatingSystem',self.lid)
        if self.args.argc()<=idx+1:
            log.error("Inverse links : Error during reading parameter 1 of IfcRelServicesBuildings, line %d"%common.counter)
            return False

        currentRefList=getIdListParam(self.args.argv[idx+1])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 1 of IfcRelServicesBuildings, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCRELSERVICESBUILDINGS','RelatedBuildings',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCRELSERVICESBUILDINGS,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatingSystem= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatedBuildings= getIdListParam(arg,spfToId)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCRELSERVICESBUILDINGS,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCRELSERVICESBUILDINGS,self).toString()       
        line += idToSPF(self.RelatingSystem)+','
        line += listParamToSPF(self.RelatedBuildings,idToSPF)+','

        return line

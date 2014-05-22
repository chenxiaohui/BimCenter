#!/usr/bin/python
#coding=utf-8
#Filename:IfcRelDefinesByProperties.py
import log
import common
from ifcreldefines import IFCRELDEFINES

from utils import *

class IFCRELDEFINESBYPROPERTIES(IFCRELDEFINES):
    """"""
    def __init__(self,id,arg):
        super(IFCRELDEFINESBYPROPERTIES,self).__init__(id,arg)
        self.type='IFCRELDEFINESBYPROPERTIES'
        self.inverse={}
        self.RelatingPropertyDefinition=None #IfcPropertySetDefinition


    def load(self):
        """register inverses"""
        if not super(IFCRELDEFINESBYPROPERTIES,self).load():
            return False
        idx=super(IFCRELDEFINESBYPROPERTIES,self).getAttrCount()
        if self.args.argc()<=idx+0:
            log.error("Inverse links : Error during reading parameter 0 of IfcRelDefinesByProperties, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+0])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 0 of IfcRelDefinesByProperties, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCRELDEFINESBYPROPERTIES','RelatingPropertyDefinition',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCRELDEFINESBYPROPERTIES,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatingPropertyDefinition= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCRELDEFINESBYPROPERTIES,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCRELDEFINESBYPROPERTIES,self).toString()       
        line += idToSPF(self.RelatingPropertyDefinition)+','

        return line

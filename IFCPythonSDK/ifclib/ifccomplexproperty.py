#!/usr/bin/python
#coding=utf-8
#Filename:IfcComplexProperty.py
import log
import common
from ifcproperty import IFCPROPERTY

from utils import *

class IFCCOMPLEXPROPERTY(IFCPROPERTY):
    """"""
    def __init__(self,id,arg):
        super(IFCCOMPLEXPROPERTY,self).__init__(id,arg)
        self.type='IFCCOMPLEXPROPERTY'
        self.inverse={}
        self.UsageName=None #IfcIdentifier
        self.HasProperties=None #SET


    def load(self):
        """register inverses"""
        if not super(IFCCOMPLEXPROPERTY,self).load():
            return False
        idx=super(IFCCOMPLEXPROPERTY,self).getAttrCount()
        if self.args.argc()<=idx+1:
            log.error("Inverse links : Error during reading parameter 1 of IfcComplexProperty, line %d"%common.counter)
            return False

        currentRefList=getIdListParam(self.args.argv[idx+1])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 1 of IfcComplexProperty, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCCOMPLEXPROPERTY','HasProperties',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCOMPLEXPROPERTY,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.UsageName= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.HasProperties= getIdListParam(arg,spfToId)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCOMPLEXPROPERTY,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCCOMPLEXPROPERTY,self).toString()       
        line += strToSPF(self.UsageName)+','
        line += listParamToSPF(self.HasProperties,idToSPF)+','

        return line

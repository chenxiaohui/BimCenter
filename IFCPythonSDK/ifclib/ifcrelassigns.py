#!/usr/bin/python
#coding=utf-8
#Filename:IfcRelAssigns.py
import log
import common
from ifcrelationship import IFCRELATIONSHIP

from utils import *

class IFCRELASSIGNS(IFCRELATIONSHIP):
    """"""
    def __init__(self,id,arg):
        super(IFCRELASSIGNS,self).__init__(id,arg)
        self.type='IFCRELASSIGNS'
        self.inverse={}
        self.RelatedObjects=None #SET
        self.RelatedObjectsType=None #IfcObjectTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCRELASSIGNS,self).load():
            return False
        idx=super(IFCRELASSIGNS,self).getAttrCount()
        if self.args.argc()<=idx+0:
            log.error("Inverse links : Error during reading parameter 0 of IfcRelAssigns, line %d"%common.counter)
            return False

        currentRefList=getIdListParam(self.args.argv[idx+0])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 0 of IfcRelAssigns, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCRELASSIGNS','RelatedObjects',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCRELASSIGNS,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatedObjects= getIdListParam(arg,spfToId)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatedObjectsType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCRELASSIGNS,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCRELASSIGNS,self).toString()       
        line += listParamToSPF(self.RelatedObjects,idToSPF)+','
        line += typerefToSPF(self.RelatedObjectsType)+','

        return line

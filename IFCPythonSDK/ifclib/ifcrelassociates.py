#!/usr/bin/python
#coding=utf-8
#Filename:IfcRelAssociates.py
import log
import common
from ifcrelationship import IFCRELATIONSHIP

from utils import *

class IFCRELASSOCIATES(IFCRELATIONSHIP):
    """"""
    def __init__(self,id,arg):
        super(IFCRELASSOCIATES,self).__init__(id,arg)
        self.type='IFCRELASSOCIATES'
        self.inverse={}
        self.RelatedObjects=None #SET


    def load(self):
        """register inverses"""
        if not super(IFCRELASSOCIATES,self).load():
            return False
        idx=super(IFCRELASSOCIATES,self).getAttrCount()
        if self.args.argc()<=idx+0:
            log.error("Inverse links : Error during reading parameter 0 of IfcRelAssociates, line %d"%common.counter)
            return False

        currentRefList=getIdListParam(self.args.argv[idx+0])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 0 of IfcRelAssociates, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCRELASSOCIATES','RelatedObjects',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCRELASSOCIATES,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatedObjects= getIdListParam(arg,spfToId)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCRELASSOCIATES,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCRELASSOCIATES,self).toString()       
        line += listParamToSPF(self.RelatedObjects,idToSPF)+','

        return line

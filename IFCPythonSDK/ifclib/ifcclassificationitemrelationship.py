#!/usr/bin/python
#coding=utf-8
#Filename:IfcClassificationItemRelationship.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCCLASSIFICATIONITEMRELATIONSHIP(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCCLASSIFICATIONITEMRELATIONSHIP,self).__init__(id,arg)
        self.type='IFCCLASSIFICATIONITEMRELATIONSHIP'
        self.inverse={}
        self.RelatingItem=None #IfcClassificationItem
        self.RelatedItems=None #SET


    def load(self):
        """register inverses"""
        if not super(IFCCLASSIFICATIONITEMRELATIONSHIP,self).load():
            return False
        idx=super(IFCCLASSIFICATIONITEMRELATIONSHIP,self).getAttrCount()
        if self.args.argc()<=idx+0:
            log.error("Inverse links : Error during reading parameter 0 of IfcClassificationItemRelationship, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+0])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 0 of IfcClassificationItemRelationship, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCCLASSIFICATIONITEMRELATIONSHIP','RelatingItem',self.lid)
        if self.args.argc()<=idx+1:
            log.error("Inverse links : Error during reading parameter 1 of IfcClassificationItemRelationship, line %d"%common.counter)
            return False

        currentRefList=getIdListParam(self.args.argv[idx+1])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 1 of IfcClassificationItemRelationship, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCCLASSIFICATIONITEMRELATIONSHIP','RelatedItems',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCLASSIFICATIONITEMRELATIONSHIP,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatingItem= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatedItems= getIdListParam(arg,spfToId)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCLASSIFICATIONITEMRELATIONSHIP,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCCLASSIFICATIONITEMRELATIONSHIP,self).toString()       
        line += idToSPF(self.RelatingItem)+','
        line += listParamToSPF(self.RelatedItems,idToSPF)+','

        return line

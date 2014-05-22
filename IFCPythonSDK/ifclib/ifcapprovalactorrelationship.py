#!/usr/bin/python
#coding=utf-8
#Filename:IfcApprovalActorRelationship.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCAPPROVALACTORRELATIONSHIP(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCAPPROVALACTORRELATIONSHIP,self).__init__(id,arg)
        self.type='IFCAPPROVALACTORRELATIONSHIP'
        self.inverse={}
        self.Actor=None #IfcActorSelect
        self.Approval=None #IfcApproval
        self.Role=None #IfcActorRole


    def load(self):
        """register inverses"""
        if not super(IFCAPPROVALACTORRELATIONSHIP,self).load():
            return False
        idx=super(IFCAPPROVALACTORRELATIONSHIP,self).getAttrCount()
        if self.args.argc()<=idx+1:
            log.error("Inverse links : Error during reading parameter 1 of IfcApprovalActorRelationship, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+1])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 1 of IfcApprovalActorRelationship, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCAPPROVALACTORRELATIONSHIP','Approval',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCAPPROVALACTORRELATIONSHIP,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Actor= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Approval= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Role= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCAPPROVALACTORRELATIONSHIP,self).getAttrCount()+3

    def toString(self):
        """"""
        line=super(IFCAPPROVALACTORRELATIONSHIP,self).toString()       
        line += typerefToSPF(self.Actor)+','
        line += idToSPF(self.Approval)+','
        line += idToSPF(self.Role)+','

        return line

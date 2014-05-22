#!/usr/bin/python
#coding=utf-8
#Filename:IfcApprovalRelationship.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCAPPROVALRELATIONSHIP(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCAPPROVALRELATIONSHIP,self).__init__(id,arg)
        self.type='IFCAPPROVALRELATIONSHIP'
        self.inverse={}
        self.RelatedApproval=None #IfcApproval
        self.RelatingApproval=None #IfcApproval
        self.Description=None #IfcText
        self.Name=None #IfcLabel


    def load(self):
        """register inverses"""
        if not super(IFCAPPROVALRELATIONSHIP,self).load():
            return False
        idx=super(IFCAPPROVALRELATIONSHIP,self).getAttrCount()
        if self.args.argc()<=idx+0:
            log.error("Inverse links : Error during reading parameter 0 of IfcApprovalRelationship, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+0])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 0 of IfcApprovalRelationship, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCAPPROVALRELATIONSHIP','RelatedApproval',self.lid)
        if self.args.argc()<=idx+1:
            log.error("Inverse links : Error during reading parameter 1 of IfcApprovalRelationship, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+1])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 1 of IfcApprovalRelationship, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCAPPROVALRELATIONSHIP','RelatingApproval',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCAPPROVALRELATIONSHIP,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatedApproval= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatingApproval= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Description= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Name= fromSPF(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCAPPROVALRELATIONSHIP,self).getAttrCount()+4

    def toString(self):
        """"""
        line=super(IFCAPPROVALRELATIONSHIP,self).toString()       
        line += idToSPF(self.RelatedApproval)+','
        line += idToSPF(self.RelatingApproval)+','
        line += strToSPF(self.Description)+','
        line += strToSPF(self.Name)+','

        return line

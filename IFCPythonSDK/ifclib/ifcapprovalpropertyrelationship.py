#!/usr/bin/python
#coding=utf-8
#Filename:IfcApprovalPropertyRelationship.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCAPPROVALPROPERTYRELATIONSHIP(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCAPPROVALPROPERTYRELATIONSHIP,self).__init__(id,arg)
        self.type='IFCAPPROVALPROPERTYRELATIONSHIP'
        self.inverse={}
        self.ApprovedProperties=None #SET
        self.Approval=None #IfcApproval


    def load(self):
        """register inverses"""
        if not super(IFCAPPROVALPROPERTYRELATIONSHIP,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCAPPROVALPROPERTYRELATIONSHIP,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ApprovedProperties= getIdListParam(arg,spfToId)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Approval= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCAPPROVALPROPERTYRELATIONSHIP,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCAPPROVALPROPERTYRELATIONSHIP,self).toString()       
        line += listParamToSPF(self.ApprovedProperties,idToSPF)+','
        line += idToSPF(self.Approval)+','

        return line

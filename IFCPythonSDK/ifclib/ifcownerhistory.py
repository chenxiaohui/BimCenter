#!/usr/bin/python
#coding=utf-8
#Filename:IfcOwnerHistory.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCOWNERHISTORY(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCOWNERHISTORY,self).__init__(id,arg)
        self.type='IFCOWNERHISTORY'
        self.inverse={}
        self.OwningUser=None #IfcPersonAndOrganization
        self.OwningApplication=None #IfcApplication
        self.State=None #IfcStateEnum
        self.ChangeAction=None #IfcChangeActionEnum
        self.LastModifiedDate=None #IfcTimeStamp
        self.LastModifyingUser=None #IfcPersonAndOrganization
        self.LastModifyingApplication=None #IfcApplication
        self.CreationDate=None #IfcTimeStamp


    def load(self):
        """register inverses"""
        if not super(IFCOWNERHISTORY,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCOWNERHISTORY,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.OwningUser= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.OwningApplication= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.State= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ChangeAction= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.LastModifiedDate= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.LastModifyingUser= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.LastModifyingApplication= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.CreationDate= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCOWNERHISTORY,self).getAttrCount()+8

    def toString(self):
        """"""
        line=super(IFCOWNERHISTORY,self).toString()       
        line += idToSPF(self.OwningUser)+','
        line += idToSPF(self.OwningApplication)+','
        line += typerefToSPF(self.State)+','
        line += typerefToSPF(self.ChangeAction)+','
        line += integerToSPF(self.LastModifiedDate)+','
        line += idToSPF(self.LastModifyingUser)+','
        line += idToSPF(self.LastModifyingApplication)+','
        line += integerToSPF(self.CreationDate)+','

        return line

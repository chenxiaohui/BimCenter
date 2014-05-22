#!/usr/bin/python
#coding=utf-8
#Filename:IfcPersonAndOrganization.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCPERSONANDORGANIZATION(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCPERSONANDORGANIZATION,self).__init__(id,arg)
        self.type='IFCPERSONANDORGANIZATION'
        self.inverse={}
        self.ThePerson=None #IfcPerson
        self.TheOrganization=None #IfcOrganization
        self.Roles=None #LIST


    def load(self):
        """register inverses"""
        if not super(IFCPERSONANDORGANIZATION,self).load():
            return False
        idx=super(IFCPERSONANDORGANIZATION,self).getAttrCount()
        if self.args.argc()<=idx+0:
            log.error("Inverse links : Error during reading parameter 0 of IfcPersonAndOrganization, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+0])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 0 of IfcPersonAndOrganization, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCPERSONANDORGANIZATION','ThePerson',self.lid)
        if self.args.argc()<=idx+1:
            log.error("Inverse links : Error during reading parameter 1 of IfcPersonAndOrganization, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+1])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 1 of IfcPersonAndOrganization, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCPERSONANDORGANIZATION','TheOrganization',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCPERSONANDORGANIZATION,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ThePerson= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.TheOrganization= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Roles= getIdListParam(arg,spfToId)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCPERSONANDORGANIZATION,self).getAttrCount()+3

    def toString(self):
        """"""
        line=super(IFCPERSONANDORGANIZATION,self).toString()       
        line += idToSPF(self.ThePerson)+','
        line += idToSPF(self.TheOrganization)+','
        line += listParamToSPF(self.Roles,idToSPF)+','

        return line

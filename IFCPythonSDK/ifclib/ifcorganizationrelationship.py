#!/usr/bin/python
#coding=utf-8
#Filename:IfcOrganizationRelationship.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCORGANIZATIONRELATIONSHIP(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCORGANIZATIONRELATIONSHIP,self).__init__(id,arg)
        self.type='IFCORGANIZATIONRELATIONSHIP'
        self.inverse={}
        self.Name=None #IfcLabel
        self.Description=None #IfcText
        self.RelatingOrganization=None #IfcOrganization
        self.RelatedOrganizations=None #SET


    def load(self):
        """register inverses"""
        if not super(IFCORGANIZATIONRELATIONSHIP,self).load():
            return False
        idx=super(IFCORGANIZATIONRELATIONSHIP,self).getAttrCount()
        if self.args.argc()<=idx+2:
            log.error("Inverse links : Error during reading parameter 2 of IfcOrganizationRelationship, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+2])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 2 of IfcOrganizationRelationship, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCORGANIZATIONRELATIONSHIP','RelatingOrganization',self.lid)
        if self.args.argc()<=idx+3:
            log.error("Inverse links : Error during reading parameter 3 of IfcOrganizationRelationship, line %d"%common.counter)
            return False

        currentRefList=getIdListParam(self.args.argv[idx+3])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 3 of IfcOrganizationRelationship, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCORGANIZATIONRELATIONSHIP','RelatedOrganizations',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCORGANIZATIONRELATIONSHIP,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Name= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Description= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatingOrganization= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatedOrganizations= getIdListParam(arg,spfToId)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCORGANIZATIONRELATIONSHIP,self).getAttrCount()+4

    def toString(self):
        """"""
        line=super(IFCORGANIZATIONRELATIONSHIP,self).toString()       
        line += strToSPF(self.Name)+','
        line += strToSPF(self.Description)+','
        line += idToSPF(self.RelatingOrganization)+','
        line += listParamToSPF(self.RelatedOrganizations,idToSPF)+','

        return line

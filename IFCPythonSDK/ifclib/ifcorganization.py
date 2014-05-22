#!/usr/bin/python
#coding=utf-8
#Filename:IfcOrganization.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCORGANIZATION(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCORGANIZATION,self).__init__(id,arg)
        self.type='IFCORGANIZATION'
        self.inverse={}
        self.Id=None #IfcIdentifier
        self.Name=None #IfcLabel
        self.Description=None #IfcText
        self.Roles=None #LIST
        self.Addresses=None #LIST
        self.inverse['IsRelatedBy']=[] #inverse:SET of IfcOrganizationRelationship
        self.inverse['Engages']=[] #inverse:SET of IfcPersonAndOrganization
        self.inverse['Relates']=[] #inverse:SET of IfcOrganizationRelationship


    def load(self):
        """register inverses"""
        if not super(IFCORGANIZATION,self).load():
            return False
        idx=super(IFCORGANIZATION,self).getAttrCount()
        if self.args.argc()<=idx+4:
            log.error("Inverse links : Error during reading parameter 4 of IfcOrganization, line %d"%common.counter)
            return False

        currentRefList=getIdListParam(self.args.argv[idx+4])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 4 of IfcOrganization, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCORGANIZATION','Addresses',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCORGANIZATION,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Id= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Name= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Description= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Roles= getIdListParam(arg,spfToId)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Addresses= getIdListParam(arg,spfToId)

        inverses = self.args.getInverses('IFCORGANIZATIONRELATIONSHIP', 'RelatedOrganizations');
        if inverses:
            self.inverse['IsRelatedBy']=inverses

        inverses = self.args.getInverses('IFCPERSONANDORGANIZATION', 'TheOrganization');
        if inverses:
            self.inverse['Engages']=inverses

        inverses = self.args.getInverses('IFCORGANIZATIONRELATIONSHIP', 'RelatingOrganization');
        if inverses:
            self.inverse['Relates']=inverses

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCORGANIZATION,self).getAttrCount()+5

    def toString(self):
        """"""
        line=super(IFCORGANIZATION,self).toString()       
        line += strToSPF(self.Id)+','
        line += strToSPF(self.Name)+','
        line += strToSPF(self.Description)+','
        line += listParamToSPF(self.Roles,idToSPF)+','
        line += listParamToSPF(self.Addresses,idToSPF)+','

        return line

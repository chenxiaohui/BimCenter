#!/usr/bin/python
#coding=utf-8
#Filename:IfcPerson.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCPERSON(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCPERSON,self).__init__(id,arg)
        self.type='IFCPERSON'
        self.inverse={}
        self.Id=None #IfcIdentifier
        self.FamilyName=None #IfcLabel
        self.GivenName=None #IfcLabel
        self.MiddleNames=None #LIST
        self.PrefixTitles=None #LIST
        self.SuffixTitles=None #LIST
        self.Roles=None #LIST
        self.Addresses=None #LIST
        self.inverse['EngagedIn']=[] #inverse:SET of IfcPersonAndOrganization


    def load(self):
        """register inverses"""
        if not super(IFCPERSON,self).load():
            return False
        idx=super(IFCPERSON,self).getAttrCount()
        if self.args.argc()<=idx+7:
            log.error("Inverse links : Error during reading parameter 7 of IfcPerson, line %d"%common.counter)
            return False

        currentRefList=getIdListParam(self.args.argv[idx+7])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 7 of IfcPerson, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCPERSON','Addresses',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCPERSON,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Id= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.FamilyName= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.GivenName= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.MiddleNames= getIdListParam(arg,fromSPF)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PrefixTitles= getIdListParam(arg,fromSPF)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.SuffixTitles= getIdListParam(arg,fromSPF)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Roles= getIdListParam(arg,spfToId)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Addresses= getIdListParam(arg,spfToId)

        inverses = self.args.getInverses('IFCPERSONANDORGANIZATION', 'ThePerson');
        if inverses:
            self.inverse['EngagedIn']=inverses

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCPERSON,self).getAttrCount()+8

    def toString(self):
        """"""
        line=super(IFCPERSON,self).toString()       
        line += strToSPF(self.Id)+','
        line += strToSPF(self.FamilyName)+','
        line += strToSPF(self.GivenName)+','
        line += listParamToSPF(self.MiddleNames,strToSPF)+','
        line += listParamToSPF(self.PrefixTitles,strToSPF)+','
        line += listParamToSPF(self.SuffixTitles,strToSPF)+','
        line += listParamToSPF(self.Roles,idToSPF)+','
        line += listParamToSPF(self.Addresses,idToSPF)+','

        return line

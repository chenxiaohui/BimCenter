#!/usr/bin/python
#coding=utf-8
#Filename:IfcLibraryInformation.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCLIBRARYINFORMATION(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCLIBRARYINFORMATION,self).__init__(id,arg)
        self.type='IFCLIBRARYINFORMATION'
        self.inverse={}
        self.Name=None #IfcLabel
        self.Version=None #IfcLabel
        self.Publisher=None #IfcOrganization
        self.VersionDate=None #IfcCalendarDate
        self.LibraryReference=None #SET


    def load(self):
        """register inverses"""
        if not super(IFCLIBRARYINFORMATION,self).load():
            return False
        idx=super(IFCLIBRARYINFORMATION,self).getAttrCount()
        if self.args.argc()<=idx+4:
            log.error("Inverse links : Error during reading parameter 4 of IfcLibraryInformation, line %d"%common.counter)
            return False

        currentRefList=getIdListParam(self.args.argv[idx+4])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 4 of IfcLibraryInformation, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCLIBRARYINFORMATION','LibraryReference',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCLIBRARYINFORMATION,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Name= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Version= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Publisher= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.VersionDate= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.LibraryReference= getIdListParam(arg,spfToId)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCLIBRARYINFORMATION,self).getAttrCount()+5

    def toString(self):
        """"""
        line=super(IFCLIBRARYINFORMATION,self).toString()       
        line += strToSPF(self.Name)+','
        line += strToSPF(self.Version)+','
        line += idToSPF(self.Publisher)+','
        line += idToSPF(self.VersionDate)+','
        line += listParamToSPF(self.LibraryReference,idToSPF)+','

        return line

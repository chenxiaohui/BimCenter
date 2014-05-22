#!/usr/bin/python
#coding=utf-8
#Filename:IfcDraughtingCalloutRelationship.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCDRAUGHTINGCALLOUTRELATIONSHIP(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCDRAUGHTINGCALLOUTRELATIONSHIP,self).__init__(id,arg)
        self.type='IFCDRAUGHTINGCALLOUTRELATIONSHIP'
        self.inverse={}
        self.Name=None #IfcLabel
        self.Description=None #IfcText
        self.RelatingDraughtingCallout=None #IfcDraughtingCallout
        self.RelatedDraughtingCallout=None #IfcDraughtingCallout


    def load(self):
        """register inverses"""
        if not super(IFCDRAUGHTINGCALLOUTRELATIONSHIP,self).load():
            return False
        idx=super(IFCDRAUGHTINGCALLOUTRELATIONSHIP,self).getAttrCount()
        if self.args.argc()<=idx+2:
            log.error("Inverse links : Error during reading parameter 2 of IfcDraughtingCalloutRelationship, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+2])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 2 of IfcDraughtingCalloutRelationship, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCDRAUGHTINGCALLOUTRELATIONSHIP','RelatingDraughtingCallout',self.lid)
        if self.args.argc()<=idx+3:
            log.error("Inverse links : Error during reading parameter 3 of IfcDraughtingCalloutRelationship, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+3])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 3 of IfcDraughtingCalloutRelationship, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCDRAUGHTINGCALLOUTRELATIONSHIP','RelatedDraughtingCallout',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCDRAUGHTINGCALLOUTRELATIONSHIP,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Name= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Description= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatingDraughtingCallout= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatedDraughtingCallout= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCDRAUGHTINGCALLOUTRELATIONSHIP,self).getAttrCount()+4

    def toString(self):
        """"""
        line=super(IFCDRAUGHTINGCALLOUTRELATIONSHIP,self).toString()       
        line += strToSPF(self.Name)+','
        line += strToSPF(self.Description)+','
        line += idToSPF(self.RelatingDraughtingCallout)+','
        line += idToSPF(self.RelatedDraughtingCallout)+','

        return line

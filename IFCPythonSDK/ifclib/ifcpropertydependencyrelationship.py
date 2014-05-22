#!/usr/bin/python
#coding=utf-8
#Filename:IfcPropertyDependencyRelationship.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCPROPERTYDEPENDENCYRELATIONSHIP(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCPROPERTYDEPENDENCYRELATIONSHIP,self).__init__(id,arg)
        self.type='IFCPROPERTYDEPENDENCYRELATIONSHIP'
        self.inverse={}
        self.DependingProperty=None #IfcProperty
        self.DependantProperty=None #IfcProperty
        self.Name=None #IfcLabel
        self.Description=None #IfcText
        self.Expression=None #IfcText


    def load(self):
        """register inverses"""
        if not super(IFCPROPERTYDEPENDENCYRELATIONSHIP,self).load():
            return False
        idx=super(IFCPROPERTYDEPENDENCYRELATIONSHIP,self).getAttrCount()
        if self.args.argc()<=idx+0:
            log.error("Inverse links : Error during reading parameter 0 of IfcPropertyDependencyRelationship, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+0])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 0 of IfcPropertyDependencyRelationship, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCPROPERTYDEPENDENCYRELATIONSHIP','DependingProperty',self.lid)
        if self.args.argc()<=idx+1:
            log.error("Inverse links : Error during reading parameter 1 of IfcPropertyDependencyRelationship, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+1])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 1 of IfcPropertyDependencyRelationship, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCPROPERTYDEPENDENCYRELATIONSHIP','DependantProperty',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCPROPERTYDEPENDENCYRELATIONSHIP,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.DependingProperty= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.DependantProperty= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Name= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Description= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Expression= fromSPF(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCPROPERTYDEPENDENCYRELATIONSHIP,self).getAttrCount()+5

    def toString(self):
        """"""
        line=super(IFCPROPERTYDEPENDENCYRELATIONSHIP,self).toString()       
        line += idToSPF(self.DependingProperty)+','
        line += idToSPF(self.DependantProperty)+','
        line += strToSPF(self.Name)+','
        line += strToSPF(self.Description)+','
        line += strToSPF(self.Expression)+','

        return line

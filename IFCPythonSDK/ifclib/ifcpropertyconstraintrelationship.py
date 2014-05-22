#!/usr/bin/python
#coding=utf-8
#Filename:IfcPropertyConstraintRelationship.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCPROPERTYCONSTRAINTRELATIONSHIP(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCPROPERTYCONSTRAINTRELATIONSHIP,self).__init__(id,arg)
        self.type='IFCPROPERTYCONSTRAINTRELATIONSHIP'
        self.inverse={}
        self.RelatingConstraint=None #IfcConstraint
        self.RelatedProperties=None #SET
        self.Name=None #IfcLabel
        self.Description=None #IfcText


    def load(self):
        """register inverses"""
        if not super(IFCPROPERTYCONSTRAINTRELATIONSHIP,self).load():
            return False
        idx=super(IFCPROPERTYCONSTRAINTRELATIONSHIP,self).getAttrCount()
        if self.args.argc()<=idx+0:
            log.error("Inverse links : Error during reading parameter 0 of IfcPropertyConstraintRelationship, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+0])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 0 of IfcPropertyConstraintRelationship, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCPROPERTYCONSTRAINTRELATIONSHIP','RelatingConstraint',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCPROPERTYCONSTRAINTRELATIONSHIP,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatingConstraint= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatedProperties= getIdListParam(arg,spfToId)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Name= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Description= fromSPF(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCPROPERTYCONSTRAINTRELATIONSHIP,self).getAttrCount()+4

    def toString(self):
        """"""
        line=super(IFCPROPERTYCONSTRAINTRELATIONSHIP,self).toString()       
        line += idToSPF(self.RelatingConstraint)+','
        line += listParamToSPF(self.RelatedProperties,idToSPF)+','
        line += strToSPF(self.Name)+','
        line += strToSPF(self.Description)+','

        return line

#!/usr/bin/python
#coding=utf-8
#Filename:IfcConstraintRelationship.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCCONSTRAINTRELATIONSHIP(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCCONSTRAINTRELATIONSHIP,self).__init__(id,arg)
        self.type='IFCCONSTRAINTRELATIONSHIP'
        self.inverse={}
        self.Name=None #IfcLabel
        self.Description=None #IfcText
        self.RelatingConstraint=None #IfcConstraint
        self.RelatedConstraints=None #SET


    def load(self):
        """register inverses"""
        if not super(IFCCONSTRAINTRELATIONSHIP,self).load():
            return False
        idx=super(IFCCONSTRAINTRELATIONSHIP,self).getAttrCount()
        if self.args.argc()<=idx+2:
            log.error("Inverse links : Error during reading parameter 2 of IfcConstraintRelationship, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+2])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 2 of IfcConstraintRelationship, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCCONSTRAINTRELATIONSHIP','RelatingConstraint',self.lid)
        if self.args.argc()<=idx+3:
            log.error("Inverse links : Error during reading parameter 3 of IfcConstraintRelationship, line %d"%common.counter)
            return False

        currentRefList=getIdListParam(self.args.argv[idx+3])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 3 of IfcConstraintRelationship, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCCONSTRAINTRELATIONSHIP','RelatedConstraints',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCONSTRAINTRELATIONSHIP,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Name= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Description= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatingConstraint= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatedConstraints= getIdListParam(arg,spfToId)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCONSTRAINTRELATIONSHIP,self).getAttrCount()+4

    def toString(self):
        """"""
        line=super(IFCCONSTRAINTRELATIONSHIP,self).toString()       
        line += strToSPF(self.Name)+','
        line += strToSPF(self.Description)+','
        line += idToSPF(self.RelatingConstraint)+','
        line += listParamToSPF(self.RelatedConstraints,idToSPF)+','

        return line

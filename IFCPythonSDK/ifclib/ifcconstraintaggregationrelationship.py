#!/usr/bin/python
#coding=utf-8
#Filename:IfcConstraintAggregationRelationship.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCCONSTRAINTAGGREGATIONRELATIONSHIP(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCCONSTRAINTAGGREGATIONRELATIONSHIP,self).__init__(id,arg)
        self.type='IFCCONSTRAINTAGGREGATIONRELATIONSHIP'
        self.inverse={}
        self.Name=None #IfcLabel
        self.Description=None #IfcText
        self.RelatingConstraint=None #IfcConstraint
        self.RelatedConstraints=None #LIST
        self.LogicalAggregator=None #IfcLogicalOperatorEnum


    def load(self):
        """register inverses"""
        if not super(IFCCONSTRAINTAGGREGATIONRELATIONSHIP,self).load():
            return False
        idx=super(IFCCONSTRAINTAGGREGATIONRELATIONSHIP,self).getAttrCount()
        if self.args.argc()<=idx+2:
            log.error("Inverse links : Error during reading parameter 2 of IfcConstraintAggregationRelationship, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+2])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 2 of IfcConstraintAggregationRelationship, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCCONSTRAINTAGGREGATIONRELATIONSHIP','RelatingConstraint',self.lid)
        if self.args.argc()<=idx+3:
            log.error("Inverse links : Error during reading parameter 3 of IfcConstraintAggregationRelationship, line %d"%common.counter)
            return False

        currentRefList=getIdListParam(self.args.argv[idx+3])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 3 of IfcConstraintAggregationRelationship, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCCONSTRAINTAGGREGATIONRELATIONSHIP','RelatedConstraints',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCONSTRAINTAGGREGATIONRELATIONSHIP,self).init():
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

        arg = self.args.getNext()
        if not isUnset(arg):
            self.LogicalAggregator= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCONSTRAINTAGGREGATIONRELATIONSHIP,self).getAttrCount()+5

    def toString(self):
        """"""
        line=super(IFCCONSTRAINTAGGREGATIONRELATIONSHIP,self).toString()       
        line += strToSPF(self.Name)+','
        line += strToSPF(self.Description)+','
        line += idToSPF(self.RelatingConstraint)+','
        line += listParamToSPF(self.RelatedConstraints,idToSPF)+','
        line += typerefToSPF(self.LogicalAggregator)+','

        return line

#!/usr/bin/python
#coding=utf-8
#Filename:IfcConstraintClassificationRelationship.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCCONSTRAINTCLASSIFICATIONRELATIONSHIP(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCCONSTRAINTCLASSIFICATIONRELATIONSHIP,self).__init__(id,arg)
        self.type='IFCCONSTRAINTCLASSIFICATIONRELATIONSHIP'
        self.inverse={}
        self.ClassifiedConstraint=None #IfcConstraint
        self.RelatedClassifications=None #SET


    def load(self):
        """register inverses"""
        if not super(IFCCONSTRAINTCLASSIFICATIONRELATIONSHIP,self).load():
            return False
        idx=super(IFCCONSTRAINTCLASSIFICATIONRELATIONSHIP,self).getAttrCount()
        if self.args.argc()<=idx+0:
            log.error("Inverse links : Error during reading parameter 0 of IfcConstraintClassificationRelationship, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+0])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 0 of IfcConstraintClassificationRelationship, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCCONSTRAINTCLASSIFICATIONRELATIONSHIP','ClassifiedConstraint',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCONSTRAINTCLASSIFICATIONRELATIONSHIP,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ClassifiedConstraint= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatedClassifications= getIdListParam(arg,spfToTypeRef)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCONSTRAINTCLASSIFICATIONRELATIONSHIP,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCCONSTRAINTCLASSIFICATIONRELATIONSHIP,self).toString()       
        line += idToSPF(self.ClassifiedConstraint)+','
        line += listParamToSPF(self.RelatedClassifications,typerefToSPF)+','

        return line

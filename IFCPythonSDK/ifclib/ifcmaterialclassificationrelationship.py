#!/usr/bin/python
#coding=utf-8
#Filename:IfcMaterialClassificationRelationship.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCMATERIALCLASSIFICATIONRELATIONSHIP(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCMATERIALCLASSIFICATIONRELATIONSHIP,self).__init__(id,arg)
        self.type='IFCMATERIALCLASSIFICATIONRELATIONSHIP'
        self.inverse={}
        self.MaterialClassifications=None #SET
        self.ClassifiedMaterial=None #IfcMaterial


    def load(self):
        """register inverses"""
        if not super(IFCMATERIALCLASSIFICATIONRELATIONSHIP,self).load():
            return False
        idx=super(IFCMATERIALCLASSIFICATIONRELATIONSHIP,self).getAttrCount()
        if self.args.argc()<=idx+1:
            log.error("Inverse links : Error during reading parameter 1 of IfcMaterialClassificationRelationship, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+1])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 1 of IfcMaterialClassificationRelationship, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCMATERIALCLASSIFICATIONRELATIONSHIP','ClassifiedMaterial',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCMATERIALCLASSIFICATIONRELATIONSHIP,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.MaterialClassifications= getIdListParam(arg,spfToTypeRef)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ClassifiedMaterial= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCMATERIALCLASSIFICATIONRELATIONSHIP,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCMATERIALCLASSIFICATIONRELATIONSHIP,self).toString()       
        line += listParamToSPF(self.MaterialClassifications,typerefToSPF)+','
        line += idToSPF(self.ClassifiedMaterial)+','

        return line

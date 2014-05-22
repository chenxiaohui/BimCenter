#!/usr/bin/python
#coding=utf-8
#Filename:IfcRepresentationMap.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCREPRESENTATIONMAP(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCREPRESENTATIONMAP,self).__init__(id,arg)
        self.type='IFCREPRESENTATIONMAP'
        self.inverse={}
        self.MappingOrigin=None #IfcAxis2Placement
        self.MappedRepresentation=None #IfcRepresentation
        self.inverse['MapUsage']=[] #inverse:SET of IfcMappedItem


    def load(self):
        """register inverses"""
        if not super(IFCREPRESENTATIONMAP,self).load():
            return False
        idx=super(IFCREPRESENTATIONMAP,self).getAttrCount()
        if self.args.argc()<=idx+1:
            log.error("Inverse links : Error during reading parameter 1 of IfcRepresentationMap, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+1])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 1 of IfcRepresentationMap, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCREPRESENTATIONMAP','MappedRepresentation',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCREPRESENTATIONMAP,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.MappingOrigin= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.MappedRepresentation= spfToId(arg)

        inverses = self.args.getInverses('IFCMAPPEDITEM', 'MappingSource');
        if inverses:
            self.inverse['MapUsage']=inverses

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCREPRESENTATIONMAP,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCREPRESENTATIONMAP,self).toString()       
        line += typerefToSPF(self.MappingOrigin)+','
        line += idToSPF(self.MappedRepresentation)+','

        return line

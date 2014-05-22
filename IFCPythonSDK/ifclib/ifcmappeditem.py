#!/usr/bin/python
#coding=utf-8
#Filename:IfcMappedItem.py
import log
import common
from ifcrepresentationitem import IFCREPRESENTATIONITEM

from utils import *

class IFCMAPPEDITEM(IFCREPRESENTATIONITEM):
    """"""
    def __init__(self,id,arg):
        super(IFCMAPPEDITEM,self).__init__(id,arg)
        self.type='IFCMAPPEDITEM'
        self.inverse={}
        self.MappingSource=None #IfcRepresentationMap
        self.MappingTarget=None #IfcCartesianTransformationOperator


    def load(self):
        """register inverses"""
        if not super(IFCMAPPEDITEM,self).load():
            return False
        idx=super(IFCMAPPEDITEM,self).getAttrCount()
        if self.args.argc()<=idx+0:
            log.error("Inverse links : Error during reading parameter 0 of IfcMappedItem, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+0])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 0 of IfcMappedItem, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCMAPPEDITEM','MappingSource',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCMAPPEDITEM,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.MappingSource= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.MappingTarget= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCMAPPEDITEM,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCMAPPEDITEM,self).toString()       
        line += idToSPF(self.MappingSource)+','
        line += idToSPF(self.MappingTarget)+','

        return line

#!/usr/bin/python
#coding=utf-8
#Filename:IfcTypeObject.py
import log
import common
from ifcobjectdefinition import IFCOBJECTDEFINITION

from utils import *

class IFCTYPEOBJECT(IFCOBJECTDEFINITION):
    """"""
    def __init__(self,id,arg):
        super(IFCTYPEOBJECT,self).__init__(id,arg)
        self.type='IFCTYPEOBJECT'
        self.inverse={}
        self.ApplicableOccurrence=None #IfcLabel
        self.HasPropertySets=None #SET
        self.inverse['ObjectTypeOf']=[] #inverse:SET of IfcRelDefinesByType


    def load(self):
        """register inverses"""
        if not super(IFCTYPEOBJECT,self).load():
            return False
        idx=super(IFCTYPEOBJECT,self).getAttrCount()
        if self.args.argc()<=idx+1:
            log.error("Inverse links : Error during reading parameter 1 of IfcTypeObject, line %d"%common.counter)
            return False

        currentRefList=getIdListParam(self.args.argv[idx+1])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 1 of IfcTypeObject, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCTYPEOBJECT','HasPropertySets',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCTYPEOBJECT,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ApplicableOccurrence= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.HasPropertySets= getIdListParam(arg,spfToId)

        inverses = self.args.getInverses('IFCRELDEFINESBYTYPE', 'RelatingType');
        if inverses:
            self.inverse['ObjectTypeOf']=inverses

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCTYPEOBJECT,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCTYPEOBJECT,self).toString()       
        line += strToSPF(self.ApplicableOccurrence)+','
        line += listParamToSPF(self.HasPropertySets,idToSPF)+','

        return line

#!/usr/bin/python
#coding=utf-8
#Filename:IfcAppliedValueRelationship.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCAPPLIEDVALUERELATIONSHIP(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCAPPLIEDVALUERELATIONSHIP,self).__init__(id,arg)
        self.type='IFCAPPLIEDVALUERELATIONSHIP'
        self.inverse={}
        self.ComponentOfTotal=None #IfcAppliedValue
        self.Components=None #SET
        self.ArithmeticOperator=None #IfcArithmeticOperatorEnum
        self.Name=None #IfcLabel
        self.Description=None #IfcText


    def load(self):
        """register inverses"""
        if not super(IFCAPPLIEDVALUERELATIONSHIP,self).load():
            return False
        idx=super(IFCAPPLIEDVALUERELATIONSHIP,self).getAttrCount()
        if self.args.argc()<=idx+0:
            log.error("Inverse links : Error during reading parameter 0 of IfcAppliedValueRelationship, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+0])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 0 of IfcAppliedValueRelationship, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCAPPLIEDVALUERELATIONSHIP','ComponentOfTotal',self.lid)
        if self.args.argc()<=idx+1:
            log.error("Inverse links : Error during reading parameter 1 of IfcAppliedValueRelationship, line %d"%common.counter)
            return False

        currentRefList=getIdListParam(self.args.argv[idx+1])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 1 of IfcAppliedValueRelationship, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCAPPLIEDVALUERELATIONSHIP','Components',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCAPPLIEDVALUERELATIONSHIP,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ComponentOfTotal= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Components= getIdListParam(arg,spfToId)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ArithmeticOperator= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Name= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Description= fromSPF(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCAPPLIEDVALUERELATIONSHIP,self).getAttrCount()+5

    def toString(self):
        """"""
        line=super(IFCAPPLIEDVALUERELATIONSHIP,self).toString()       
        line += idToSPF(self.ComponentOfTotal)+','
        line += listParamToSPF(self.Components,idToSPF)+','
        line += typerefToSPF(self.ArithmeticOperator)+','
        line += strToSPF(self.Name)+','
        line += strToSPF(self.Description)+','

        return line

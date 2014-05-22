#!/usr/bin/python
#coding=utf-8
#Filename:IfcReferencesValueDocument.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCREFERENCESVALUEDOCUMENT(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCREFERENCESVALUEDOCUMENT,self).__init__(id,arg)
        self.type='IFCREFERENCESVALUEDOCUMENT'
        self.inverse={}
        self.ReferencedDocument=None #IfcDocumentSelect
        self.ReferencingValues=None #SET
        self.Name=None #IfcLabel
        self.Description=None #IfcText


    def load(self):
        """register inverses"""
        if not super(IFCREFERENCESVALUEDOCUMENT,self).load():
            return False
        idx=super(IFCREFERENCESVALUEDOCUMENT,self).getAttrCount()
        if self.args.argc()<=idx+1:
            log.error("Inverse links : Error during reading parameter 1 of IfcReferencesValueDocument, line %d"%common.counter)
            return False

        currentRefList=getIdListParam(self.args.argv[idx+1])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 1 of IfcReferencesValueDocument, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCREFERENCESVALUEDOCUMENT','ReferencingValues',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCREFERENCESVALUEDOCUMENT,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ReferencedDocument= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ReferencingValues= getIdListParam(arg,spfToId)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Name= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Description= fromSPF(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCREFERENCESVALUEDOCUMENT,self).getAttrCount()+4

    def toString(self):
        """"""
        line=super(IFCREFERENCESVALUEDOCUMENT,self).toString()       
        line += typerefToSPF(self.ReferencedDocument)+','
        line += listParamToSPF(self.ReferencingValues,idToSPF)+','
        line += strToSPF(self.Name)+','
        line += strToSPF(self.Description)+','

        return line

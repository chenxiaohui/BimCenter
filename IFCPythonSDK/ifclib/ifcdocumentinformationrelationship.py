#!/usr/bin/python
#coding=utf-8
#Filename:IfcDocumentInformationRelationship.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCDOCUMENTINFORMATIONRELATIONSHIP(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCDOCUMENTINFORMATIONRELATIONSHIP,self).__init__(id,arg)
        self.type='IFCDOCUMENTINFORMATIONRELATIONSHIP'
        self.inverse={}
        self.RelatingDocument=None #IfcDocumentInformation
        self.RelatedDocuments=None #SET
        self.RelationshipType=None #IfcLabel


    def load(self):
        """register inverses"""
        if not super(IFCDOCUMENTINFORMATIONRELATIONSHIP,self).load():
            return False
        idx=super(IFCDOCUMENTINFORMATIONRELATIONSHIP,self).getAttrCount()
        if self.args.argc()<=idx+0:
            log.error("Inverse links : Error during reading parameter 0 of IfcDocumentInformationRelationship, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+0])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 0 of IfcDocumentInformationRelationship, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCDOCUMENTINFORMATIONRELATIONSHIP','RelatingDocument',self.lid)
        if self.args.argc()<=idx+1:
            log.error("Inverse links : Error during reading parameter 1 of IfcDocumentInformationRelationship, line %d"%common.counter)
            return False

        currentRefList=getIdListParam(self.args.argv[idx+1])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 1 of IfcDocumentInformationRelationship, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCDOCUMENTINFORMATIONRELATIONSHIP','RelatedDocuments',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCDOCUMENTINFORMATIONRELATIONSHIP,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatingDocument= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatedDocuments= getIdListParam(arg,spfToId)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelationshipType= fromSPF(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCDOCUMENTINFORMATIONRELATIONSHIP,self).getAttrCount()+3

    def toString(self):
        """"""
        line=super(IFCDOCUMENTINFORMATIONRELATIONSHIP,self).toString()       
        line += idToSPF(self.RelatingDocument)+','
        line += listParamToSPF(self.RelatedDocuments,idToSPF)+','
        line += strToSPF(self.RelationshipType)+','

        return line

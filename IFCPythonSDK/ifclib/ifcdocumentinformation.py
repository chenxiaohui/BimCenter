#!/usr/bin/python
#coding=utf-8
#Filename:IfcDocumentInformation.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCDOCUMENTINFORMATION(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCDOCUMENTINFORMATION,self).__init__(id,arg)
        self.type='IFCDOCUMENTINFORMATION'
        self.inverse={}
        self.DocumentId=None #IfcIdentifier
        self.Name=None #IfcLabel
        self.Description=None #IfcText
        self.DocumentReferences=None #SET
        self.Purpose=None #IfcText
        self.IntendedUse=None #IfcText
        self.Scope=None #IfcText
        self.Revision=None #IfcLabel
        self.DocumentOwner=None #IfcActorSelect
        self.Editors=None #SET
        self.CreationTime=None #IfcDateAndTime
        self.LastRevisionTime=None #IfcDateAndTime
        self.ElectronicFormat=None #IfcDocumentElectronicFormat
        self.ValidFrom=None #IfcCalendarDate
        self.ValidUntil=None #IfcCalendarDate
        self.Confidentiality=None #IfcDocumentConfidentialityEnum
        self.Status=None #IfcDocumentStatusEnum
        self.inverse['IsPointer']=[] #inverse:SET of IfcDocumentInformationRelationship
        self.inverse['IsPointedTo']=[] #inverse:SET of IfcDocumentInformationRelationship


    def load(self):
        """register inverses"""
        if not super(IFCDOCUMENTINFORMATION,self).load():
            return False
        idx=super(IFCDOCUMENTINFORMATION,self).getAttrCount()
        if self.args.argc()<=idx+3:
            log.error("Inverse links : Error during reading parameter 3 of IfcDocumentInformation, line %d"%common.counter)
            return False

        currentRefList=getIdListParam(self.args.argv[idx+3])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 3 of IfcDocumentInformation, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCDOCUMENTINFORMATION','DocumentReferences',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCDOCUMENTINFORMATION,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.DocumentId= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Name= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Description= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.DocumentReferences= getIdListParam(arg,spfToId)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Purpose= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.IntendedUse= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Scope= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Revision= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.DocumentOwner= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Editors= getIdListParam(arg,spfToTypeRef)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.CreationTime= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.LastRevisionTime= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ElectronicFormat= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ValidFrom= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ValidUntil= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Confidentiality= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Status= spfToTypeRef(arg)

        inverses = self.args.getInverses('IFCDOCUMENTINFORMATIONRELATIONSHIP', 'RelatingDocument');
        if inverses:
            self.inverse['IsPointer']=inverses

        inverses = self.args.getInverses('IFCDOCUMENTINFORMATIONRELATIONSHIP', 'RelatedDocuments');
        if inverses:
            self.inverse['IsPointedTo']=inverses

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCDOCUMENTINFORMATION,self).getAttrCount()+17

    def toString(self):
        """"""
        line=super(IFCDOCUMENTINFORMATION,self).toString()       
        line += strToSPF(self.DocumentId)+','
        line += strToSPF(self.Name)+','
        line += strToSPF(self.Description)+','
        line += listParamToSPF(self.DocumentReferences,idToSPF)+','
        line += strToSPF(self.Purpose)+','
        line += strToSPF(self.IntendedUse)+','
        line += strToSPF(self.Scope)+','
        line += strToSPF(self.Revision)+','
        line += typerefToSPF(self.DocumentOwner)+','
        line += listParamToSPF(self.Editors,typerefToSPF)+','
        line += idToSPF(self.CreationTime)+','
        line += idToSPF(self.LastRevisionTime)+','
        line += idToSPF(self.ElectronicFormat)+','
        line += idToSPF(self.ValidFrom)+','
        line += idToSPF(self.ValidUntil)+','
        line += typerefToSPF(self.Confidentiality)+','
        line += typerefToSPF(self.Status)+','

        return line

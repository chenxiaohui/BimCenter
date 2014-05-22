#!/usr/bin/python
#coding=utf-8
#Filename:IfcApproval.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCAPPROVAL(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCAPPROVAL,self).__init__(id,arg)
        self.type='IFCAPPROVAL'
        self.inverse={}
        self.Description=None #IfcText
        self.ApprovalDateTime=None #IfcDateTimeSelect
        self.ApprovalStatus=None #IfcLabel
        self.ApprovalLevel=None #IfcLabel
        self.ApprovalQualifier=None #IfcText
        self.Name=None #IfcLabel
        self.Identifier=None #IfcIdentifier
        self.inverse['IsRelatedWith']=[] #inverse:SET of IfcApprovalRelationship
        self.inverse['Actors']=[] #inverse:SET of IfcApprovalActorRelationship
        self.inverse['Relates']=[] #inverse:SET of IfcApprovalRelationship


    def load(self):
        """register inverses"""
        if not super(IFCAPPROVAL,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCAPPROVAL,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Description= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ApprovalDateTime= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ApprovalStatus= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ApprovalLevel= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ApprovalQualifier= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Name= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Identifier= fromSPF(arg)

        inverses = self.args.getInverses('IFCAPPROVALRELATIONSHIP', 'RelatedApproval');
        if inverses:
            self.inverse['IsRelatedWith']=inverses

        inverses = self.args.getInverses('IFCAPPROVALACTORRELATIONSHIP', 'Approval');
        if inverses:
            self.inverse['Actors']=inverses

        inverses = self.args.getInverses('IFCAPPROVALRELATIONSHIP', 'RelatingApproval');
        if inverses:
            self.inverse['Relates']=inverses

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCAPPROVAL,self).getAttrCount()+7

    def toString(self):
        """"""
        line=super(IFCAPPROVAL,self).toString()       
        line += strToSPF(self.Description)+','
        line += typerefToSPF(self.ApprovalDateTime)+','
        line += strToSPF(self.ApprovalStatus)+','
        line += strToSPF(self.ApprovalLevel)+','
        line += strToSPF(self.ApprovalQualifier)+','
        line += strToSPF(self.Name)+','
        line += strToSPF(self.Identifier)+','

        return line

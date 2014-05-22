#!/usr/bin/python
#coding=utf-8
#Filename:IfcAppliedValue.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCAPPLIEDVALUE(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCAPPLIEDVALUE,self).__init__(id,arg)
        self.type='IFCAPPLIEDVALUE'
        self.inverse={}
        self.Name=None #IfcLabel
        self.Description=None #IfcText
        self.AppliedValue=None #IfcAppliedValueSelect
        self.UnitBasis=None #IfcMeasureWithUnit
        self.ApplicableDate=None #IfcDateTimeSelect
        self.FixedUntilDate=None #IfcDateTimeSelect
        self.inverse['ValueOfComponents']=[] #inverse:SET of IfcAppliedValueRelationship
        self.inverse['IsComponentIn']=[] #inverse:SET of IfcAppliedValueRelationship
        self.inverse['ValuesReferenced']=[] #inverse:SET of IfcReferencesValueDocument


    def load(self):
        """register inverses"""
        if not super(IFCAPPLIEDVALUE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCAPPLIEDVALUE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Name= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Description= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.AppliedValue= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.UnitBasis= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ApplicableDate= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.FixedUntilDate= spfToTypeRef(arg)

        inverses = self.args.getInverses('IFCAPPLIEDVALUERELATIONSHIP', 'ComponentOfTotal');
        if inverses:
            self.inverse['ValueOfComponents']=inverses

        inverses = self.args.getInverses('IFCAPPLIEDVALUERELATIONSHIP', 'Components');
        if inverses:
            self.inverse['IsComponentIn']=inverses

        inverses = self.args.getInverses('IFCREFERENCESVALUEDOCUMENT', 'ReferencingValues');
        if inverses:
            self.inverse['ValuesReferenced']=inverses

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCAPPLIEDVALUE,self).getAttrCount()+6

    def toString(self):
        """"""
        line=super(IFCAPPLIEDVALUE,self).toString()       
        line += strToSPF(self.Name)+','
        line += strToSPF(self.Description)+','
        line += typerefToSPF(self.AppliedValue)+','
        line += idToSPF(self.UnitBasis)+','
        line += typerefToSPF(self.ApplicableDate)+','
        line += typerefToSPF(self.FixedUntilDate)+','

        return line

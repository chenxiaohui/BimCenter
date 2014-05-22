#!/usr/bin/python
#coding=utf-8
#Filename:IfcProperty.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCPROPERTY(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCPROPERTY,self).__init__(id,arg)
        self.type='IFCPROPERTY'
        self.inverse={}
        self.Name=None #IfcIdentifier
        self.Description=None #IfcText
        self.inverse['PartOfComplex']=[] #inverse:SET of IfcComplexProperty
        self.inverse['PropertyForDependance']=[] #inverse:SET of IfcPropertyDependencyRelationship
        self.inverse['PropertyDependsOn']=[] #inverse:SET of IfcPropertyDependencyRelationship


    def load(self):
        """register inverses"""
        if not super(IFCPROPERTY,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCPROPERTY,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Name= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Description= fromSPF(arg)

        inverses = self.args.getInverses('IFCCOMPLEXPROPERTY', 'HasProperties');
        if inverses:
            self.inverse['PartOfComplex']=inverses

        inverses = self.args.getInverses('IFCPROPERTYDEPENDENCYRELATIONSHIP', 'DependingProperty');
        if inverses:
            self.inverse['PropertyForDependance']=inverses

        inverses = self.args.getInverses('IFCPROPERTYDEPENDENCYRELATIONSHIP', 'DependantProperty');
        if inverses:
            self.inverse['PropertyDependsOn']=inverses

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCPROPERTY,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCPROPERTY,self).toString()       
        line += strToSPF(self.Name)+','
        line += strToSPF(self.Description)+','

        return line

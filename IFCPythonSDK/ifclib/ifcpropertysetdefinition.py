#!/usr/bin/python
#coding=utf-8
#Filename:IfcPropertySetDefinition.py
import log
import common
from ifcpropertydefinition import IFCPROPERTYDEFINITION

from utils import *

class IFCPROPERTYSETDEFINITION(IFCPROPERTYDEFINITION):
    """"""
    def __init__(self,id,arg):
        super(IFCPROPERTYSETDEFINITION,self).__init__(id,arg)
        self.type='IFCPROPERTYSETDEFINITION'
        self.inverse={}
        self.inverse['DefinesType']=[] #inverse:SET of IfcTypeObject
        self.inverse['PropertyDefinitionOf']=[] #inverse:SET of IfcRelDefinesByProperties


    def load(self):
        """register inverses"""
        if not super(IFCPROPERTYSETDEFINITION,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCPROPERTYSETDEFINITION,self).init():
            return False

        inverses = self.args.getInverses('IFCTYPEOBJECT', 'HasPropertySets');
        if inverses:
            self.inverse['DefinesType']=inverses

        inverses = self.args.getInverses('IFCRELDEFINESBYPROPERTIES', 'RelatingPropertyDefinition');
        if inverses:
            self.inverse['PropertyDefinitionOf']=inverses

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCPROPERTYSETDEFINITION,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCPROPERTYSETDEFINITION,self).toString()       

        return line

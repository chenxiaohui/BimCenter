#!/usr/bin/python
#coding=utf-8
#Filename:IfcPropertyDefinition.py
import log
import common
from ifcroot import IFCROOT

from utils import *

class IFCPROPERTYDEFINITION(IFCROOT):
    """"""
    def __init__(self,id,arg):
        super(IFCPROPERTYDEFINITION,self).__init__(id,arg)
        self.type='IFCPROPERTYDEFINITION'
        self.inverse={}
        self.inverse['HasAssociations']=[] #inverse:SET of IfcRelAssociates


    def load(self):
        """register inverses"""
        if not super(IFCPROPERTYDEFINITION,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCPROPERTYDEFINITION,self).init():
            return False

        inverses = self.args.getInverses('IFCRELASSOCIATES', 'RelatedObjects');
        if inverses:
            self.inverse['HasAssociations']=inverses

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCPROPERTYDEFINITION,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCPROPERTYDEFINITION,self).toString()       

        return line

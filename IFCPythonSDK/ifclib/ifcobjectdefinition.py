#!/usr/bin/python
#coding=utf-8
#Filename:IfcObjectDefinition.py
import log
import common
from ifcroot import IFCROOT

from utils import *

class IFCOBJECTDEFINITION(IFCROOT):
    """"""
    def __init__(self,id,arg):
        super(IFCOBJECTDEFINITION,self).__init__(id,arg)
        self.type='IFCOBJECTDEFINITION'
        self.inverse={}
        self.inverse['IsDecomposedBy']=[] #inverse:SET of IfcRelDecomposes
        self.inverse['Decomposes']=[] #inverse:SET of IfcRelDecomposes
        self.inverse['HasAssignments']=[] #inverse:SET of IfcRelAssigns
        self.inverse['HasAssociations']=[] #inverse:SET of IfcRelAssociates


    def load(self):
        """register inverses"""
        if not super(IFCOBJECTDEFINITION,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCOBJECTDEFINITION,self).init():
            return False

        inverses = self.args.getInverses('IFCRELDECOMPOSES', 'RelatingObject');
        if inverses:
            self.inverse['IsDecomposedBy']=inverses

        inverses = self.args.getInverses('IFCRELDECOMPOSES', 'RelatedObjects');
        if inverses:
            self.inverse['Decomposes']=inverses

        inverses = self.args.getInverses('IFCRELASSIGNS', 'RelatedObjects');
        if inverses:
            self.inverse['HasAssignments']=inverses

        inverses = self.args.getInverses('IFCRELASSOCIATES', 'RelatedObjects');
        if inverses:
            self.inverse['HasAssociations']=inverses

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCOBJECTDEFINITION,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCOBJECTDEFINITION,self).toString()       

        return line

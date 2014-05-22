#!/usr/bin/python
#coding=utf-8
#Filename:IfcMaterial.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCMATERIAL(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCMATERIAL,self).__init__(id,arg)
        self.type='IFCMATERIAL'
        self.inverse={}
        self.Name=None #IfcLabel
        self.inverse['ClassifiedAs']=[] #inverse:SET of IfcMaterialClassificationRelationship
        self.inverse['HasRepresentation']=[] #inverse:SET of IfcMaterialDefinitionRepresentation


    def load(self):
        """register inverses"""
        if not super(IFCMATERIAL,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCMATERIAL,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Name= fromSPF(arg)

        inverses = self.args.getInverses('IFCMATERIALCLASSIFICATIONRELATIONSHIP', 'ClassifiedMaterial');
        if inverses:
            self.inverse['ClassifiedAs']=inverses

        inverses = self.args.getInverses('IFCMATERIALDEFINITIONREPRESENTATION', 'RepresentedMaterial');
        if inverses:
            self.inverse['HasRepresentation']=inverses

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCMATERIAL,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCMATERIAL,self).toString()       
        line += strToSPF(self.Name)+','

        return line

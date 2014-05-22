#!/usr/bin/python
#coding=utf-8
#Filename:IfcSpatialStructureElement.py
import log
import common
from ifcproduct import IFCPRODUCT

from utils import *

class IFCSPATIALSTRUCTUREELEMENT(IFCPRODUCT):
    """"""
    def __init__(self,id,arg):
        super(IFCSPATIALSTRUCTUREELEMENT,self).__init__(id,arg)
        self.type='IFCSPATIALSTRUCTUREELEMENT'
        self.inverse={}
        self.LongName=None #IfcLabel
        self.CompositionType=None #IfcElementCompositionEnum
        self.inverse['ContainsElements']=[] #inverse:SET of IfcRelContainedInSpatialStructure
        self.inverse['ReferencesElements']=[] #inverse:SET of IfcRelReferencedInSpatialStructure
        self.inverse['ServicedBySystems']=[] #inverse:SET of IfcRelServicesBuildings


    def load(self):
        """register inverses"""
        if not super(IFCSPATIALSTRUCTUREELEMENT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSPATIALSTRUCTUREELEMENT,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.LongName= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.CompositionType= spfToTypeRef(arg)

        inverses = self.args.getInverses('IFCRELCONTAINEDINSPATIALSTRUCTURE', 'RelatingStructure');
        if inverses:
            self.inverse['ContainsElements']=inverses

        inverses = self.args.getInverses('IFCRELREFERENCEDINSPATIALSTRUCTURE', 'RelatingStructure');
        if inverses:
            self.inverse['ReferencesElements']=inverses

        inverses = self.args.getInverses('IFCRELSERVICESBUILDINGS', 'RelatedBuildings');
        if inverses:
            self.inverse['ServicedBySystems']=inverses

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSPATIALSTRUCTUREELEMENT,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCSPATIALSTRUCTUREELEMENT,self).toString()       
        line += strToSPF(self.LongName)+','
        line += typerefToSPF(self.CompositionType)+','

        return line

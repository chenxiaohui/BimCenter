#!/usr/bin/python
#coding=utf-8
#Filename:IfcElement.py
import log
import common
from ifcproduct import IFCPRODUCT

from utils import *

class IFCELEMENT(IFCPRODUCT):
    """"""
    def __init__(self,id,arg):
        super(IFCELEMENT,self).__init__(id,arg)
        self.type='IFCELEMENT'
        self.inverse={}
        self.Tag=None #IfcIdentifier
        self.inverse['HasOpenings']=[] #inverse:SET of IfcRelVoidsElement
        self.inverse['HasPorts']=[] #inverse:SET of IfcRelConnectsPortToElement
        self.inverse['HasStructuralMember']=[] #inverse:SET of IfcRelConnectsStructuralElement
        self.inverse['IsConnectionRealization']=[] #inverse:SET of IfcRelConnectsWithRealizingElements
        self.inverse['ReferencedInStructures']=[] #inverse:SET of IfcRelReferencedInSpatialStructure
        self.inverse['ConnectedTo']=[] #inverse:SET of IfcRelConnectsElements
        self.inverse['FillsVoids']=[] #inverse:SET of IfcRelFillsElement
        self.inverse['HasProjections']=[] #inverse:SET of IfcRelProjectsElement
        self.inverse['ConnectedFrom']=[] #inverse:SET of IfcRelConnectsElements
        self.inverse['HasCoverings']=[] #inverse:SET of IfcRelCoversBldgElements
        self.inverse['ContainedInStructure']=[] #inverse:SET of IfcRelContainedInSpatialStructure
        self.inverse['ProvidesBoundaries']=[] #inverse:SET of IfcRelSpaceBoundary


    def load(self):
        """register inverses"""
        if not super(IFCELEMENT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCELEMENT,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Tag= fromSPF(arg)

        inverses = self.args.getInverses('IFCRELVOIDSELEMENT', 'RelatingBuildingElement');
        if inverses:
            self.inverse['HasOpenings']=inverses

        inverses = self.args.getInverses('IFCRELCONNECTSPORTTOELEMENT', 'RelatedElement');
        if inverses:
            self.inverse['HasPorts']=inverses

        inverses = self.args.getInverses('IFCRELCONNECTSSTRUCTURALELEMENT', 'RelatingElement');
        if inverses:
            self.inverse['HasStructuralMember']=inverses

        inverses = self.args.getInverses('IFCRELCONNECTSWITHREALIZINGELEMENTS', 'RealizingElements');
        if inverses:
            self.inverse['IsConnectionRealization']=inverses

        inverses = self.args.getInverses('IFCRELREFERENCEDINSPATIALSTRUCTURE', 'RelatedElements');
        if inverses:
            self.inverse['ReferencedInStructures']=inverses

        inverses = self.args.getInverses('IFCRELCONNECTSELEMENTS', 'RelatingElement');
        if inverses:
            self.inverse['ConnectedTo']=inverses

        inverses = self.args.getInverses('IFCRELFILLSELEMENT', 'RelatedBuildingElement');
        if inverses:
            self.inverse['FillsVoids']=inverses

        inverses = self.args.getInverses('IFCRELPROJECTSELEMENT', 'RelatingElement');
        if inverses:
            self.inverse['HasProjections']=inverses

        inverses = self.args.getInverses('IFCRELCONNECTSELEMENTS', 'RelatedElement');
        if inverses:
            self.inverse['ConnectedFrom']=inverses

        inverses = self.args.getInverses('IFCRELCOVERSBLDGELEMENTS', 'RelatingBuildingElement');
        if inverses:
            self.inverse['HasCoverings']=inverses

        inverses = self.args.getInverses('IFCRELCONTAINEDINSPATIALSTRUCTURE', 'RelatedElements');
        if inverses:
            self.inverse['ContainedInStructure']=inverses

        inverses = self.args.getInverses('IFCRELSPACEBOUNDARY', 'RelatedBuildingElement');
        if inverses:
            self.inverse['ProvidesBoundaries']=inverses

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCELEMENT,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCELEMENT,self).toString()       
        line += strToSPF(self.Tag)+','

        return line

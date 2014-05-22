#!/usr/bin/python
#coding=utf-8
#Filename:IfcSpaceProgram.py
import log
import common
from ifccontrol import IFCCONTROL

from utils import *

class IFCSPACEPROGRAM(IFCCONTROL):
    """"""
    def __init__(self,id,arg):
        super(IFCSPACEPROGRAM,self).__init__(id,arg)
        self.type='IFCSPACEPROGRAM'
        self.inverse={}
        self.SpaceProgramIdentifier=None #IfcIdentifier
        self.MaxRequiredArea=None #IfcAreaMeasure
        self.MinRequiredArea=None #IfcAreaMeasure
        self.RequestedLocation=None #IfcSpatialStructureElement
        self.StandardRequiredArea=None #IfcAreaMeasure
        self.inverse['HasInteractionReqsTo']=[] #inverse:SET of IfcRelInteractionRequirements
        self.inverse['HasInteractionReqsFrom']=[] #inverse:SET of IfcRelInteractionRequirements


    def load(self):
        """register inverses"""
        if not super(IFCSPACEPROGRAM,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSPACEPROGRAM,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.SpaceProgramIdentifier= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.MaxRequiredArea= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.MinRequiredArea= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RequestedLocation= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.StandardRequiredArea= spfToInteger(arg)

        inverses = self.args.getInverses('IFCRELINTERACTIONREQUIREMENTS', 'RelatingSpaceProgram');
        if inverses:
            self.inverse['HasInteractionReqsTo']=inverses

        inverses = self.args.getInverses('IFCRELINTERACTIONREQUIREMENTS', 'RelatedSpaceProgram');
        if inverses:
            self.inverse['HasInteractionReqsFrom']=inverses

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSPACEPROGRAM,self).getAttrCount()+5

    def toString(self):
        """"""
        line=super(IFCSPACEPROGRAM,self).toString()       
        line += strToSPF(self.SpaceProgramIdentifier)+','
        line += integerToSPF(self.MaxRequiredArea)+','
        line += integerToSPF(self.MinRequiredArea)+','
        line += idToSPF(self.RequestedLocation)+','
        line += integerToSPF(self.StandardRequiredArea)+','

        return line

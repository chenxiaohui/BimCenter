#!/usr/bin/python
#coding=utf-8
#Filename:IfcRelInteractionRequirements.py
import log
import common
from ifcrelconnects import IFCRELCONNECTS

from utils import *

class IFCRELINTERACTIONREQUIREMENTS(IFCRELCONNECTS):
    """"""
    def __init__(self,id,arg):
        super(IFCRELINTERACTIONREQUIREMENTS,self).__init__(id,arg)
        self.type='IFCRELINTERACTIONREQUIREMENTS'
        self.inverse={}
        self.DailyInteraction=None #IfcCountMeasure
        self.ImportanceRating=None #IfcNormalisedRatioMeasure
        self.LocationOfInteraction=None #IfcSpatialStructureElement
        self.RelatedSpaceProgram=None #IfcSpaceProgram
        self.RelatingSpaceProgram=None #IfcSpaceProgram


    def load(self):
        """register inverses"""
        if not super(IFCRELINTERACTIONREQUIREMENTS,self).load():
            return False
        idx=super(IFCRELINTERACTIONREQUIREMENTS,self).getAttrCount()
        if self.args.argc()<=idx+3:
            log.error("Inverse links : Error during reading parameter 3 of IfcRelInteractionRequirements, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+3])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 3 of IfcRelInteractionRequirements, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCRELINTERACTIONREQUIREMENTS','RelatedSpaceProgram',self.lid)
        if self.args.argc()<=idx+4:
            log.error("Inverse links : Error during reading parameter 4 of IfcRelInteractionRequirements, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+4])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 4 of IfcRelInteractionRequirements, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCRELINTERACTIONREQUIREMENTS','RelatingSpaceProgram',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCRELINTERACTIONREQUIREMENTS,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.DailyInteraction= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ImportanceRating= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.LocationOfInteraction= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatedSpaceProgram= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatingSpaceProgram= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCRELINTERACTIONREQUIREMENTS,self).getAttrCount()+5

    def toString(self):
        """"""
        line=super(IFCRELINTERACTIONREQUIREMENTS,self).toString()       
        line += integerToSPF(self.DailyInteraction)+','
        line += integerToSPF(self.ImportanceRating)+','
        line += idToSPF(self.LocationOfInteraction)+','
        line += idToSPF(self.RelatedSpaceProgram)+','
        line += idToSPF(self.RelatingSpaceProgram)+','

        return line

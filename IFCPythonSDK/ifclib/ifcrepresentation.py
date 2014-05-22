#!/usr/bin/python
#coding=utf-8
#Filename:IfcRepresentation.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCREPRESENTATION(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCREPRESENTATION,self).__init__(id,arg)
        self.type='IFCREPRESENTATION'
        self.inverse={}
        self.ContextOfItems=None #IfcRepresentationContext
        self.RepresentationIdentifier=None #IfcLabel
        self.RepresentationType=None #IfcLabel
        self.Items=None #SET
        self.inverse['OfProductRepresentation']=[] #inverse:SET of IfcProductRepresentation
        self.inverse['RepresentationMap']=[] #inverse:SET of IfcRepresentationMap
        self.inverse['LayerAssignments']=[] #inverse:SET of IfcPresentationLayerAssignment


    def load(self):
        """register inverses"""
        if not super(IFCREPRESENTATION,self).load():
            return False
        idx=super(IFCREPRESENTATION,self).getAttrCount()
        if self.args.argc()<=idx+0:
            log.error("Inverse links : Error during reading parameter 0 of IfcRepresentation, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+0])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 0 of IfcRepresentation, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCREPRESENTATION','ContextOfItems',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCREPRESENTATION,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ContextOfItems= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RepresentationIdentifier= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RepresentationType= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Items= getIdListParam(arg,spfToId)

        inverses = self.args.getInverses('IFCPRODUCTREPRESENTATION', 'Representations');
        if inverses:
            self.inverse['OfProductRepresentation']=inverses

        inverses = self.args.getInverses('IFCREPRESENTATIONMAP', 'MappedRepresentation');
        if inverses:
            self.inverse['RepresentationMap']=inverses

        inverses = self.args.getInverses('IFCPRESENTATIONLAYERASSIGNMENT', 'AssignedItems');
        if inverses:
            self.inverse['LayerAssignments']=inverses

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCREPRESENTATION,self).getAttrCount()+4

    def toString(self):
        """"""
        line=super(IFCREPRESENTATION,self).toString()       
        line += idToSPF(self.ContextOfItems)+','
        line += strToSPF(self.RepresentationIdentifier)+','
        line += strToSPF(self.RepresentationType)+','
        line += listParamToSPF(self.Items,idToSPF)+','

        return line

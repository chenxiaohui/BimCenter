#!/usr/bin/python
#coding=utf-8
#Filename:IfcPresentationLayerAssignment.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCPRESENTATIONLAYERASSIGNMENT(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCPRESENTATIONLAYERASSIGNMENT,self).__init__(id,arg)
        self.type='IFCPRESENTATIONLAYERASSIGNMENT'
        self.inverse={}
        self.Name=None #IfcLabel
        self.Description=None #IfcText
        self.AssignedItems=None #SET
        self.Identifier=None #IfcIdentifier


    def load(self):
        """register inverses"""
        if not super(IFCPRESENTATIONLAYERASSIGNMENT,self).load():
            return False
        idx=super(IFCPRESENTATIONLAYERASSIGNMENT,self).getAttrCount()
        if self.args.argc()<=idx+2:
            log.error("Inverse links : Error during reading parameter 2 of IfcPresentationLayerAssignment, line %d"%common.counter)
            return False

        currentRefList=getIdListParam(self.args.argv[idx+2])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 2 of IfcPresentationLayerAssignment, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCPRESENTATIONLAYERASSIGNMENT','AssignedItems',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCPRESENTATIONLAYERASSIGNMENT,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Name= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Description= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.AssignedItems= getIdListParam(arg,spfToTypeRef)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Identifier= fromSPF(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCPRESENTATIONLAYERASSIGNMENT,self).getAttrCount()+4

    def toString(self):
        """"""
        line=super(IFCPRESENTATIONLAYERASSIGNMENT,self).toString()       
        line += strToSPF(self.Name)+','
        line += strToSPF(self.Description)+','
        line += listParamToSPF(self.AssignedItems,typerefToSPF)+','
        line += strToSPF(self.Identifier)+','

        return line

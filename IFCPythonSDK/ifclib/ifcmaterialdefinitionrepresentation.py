#!/usr/bin/python
#coding=utf-8
#Filename:IfcMaterialDefinitionRepresentation.py
import log
import common
from ifcproductrepresentation import IFCPRODUCTREPRESENTATION

from utils import *

class IFCMATERIALDEFINITIONREPRESENTATION(IFCPRODUCTREPRESENTATION):
    """"""
    def __init__(self,id,arg):
        super(IFCMATERIALDEFINITIONREPRESENTATION,self).__init__(id,arg)
        self.type='IFCMATERIALDEFINITIONREPRESENTATION'
        self.inverse={}
        self.RepresentedMaterial=None #IfcMaterial


    def load(self):
        """register inverses"""
        if not super(IFCMATERIALDEFINITIONREPRESENTATION,self).load():
            return False
        idx=super(IFCMATERIALDEFINITIONREPRESENTATION,self).getAttrCount()
        if self.args.argc()<=idx+0:
            log.error("Inverse links : Error during reading parameter 0 of IfcMaterialDefinitionRepresentation, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+0])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 0 of IfcMaterialDefinitionRepresentation, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCMATERIALDEFINITIONREPRESENTATION','RepresentedMaterial',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCMATERIALDEFINITIONREPRESENTATION,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RepresentedMaterial= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCMATERIALDEFINITIONREPRESENTATION,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCMATERIALDEFINITIONREPRESENTATION,self).toString()       
        line += idToSPF(self.RepresentedMaterial)+','

        return line

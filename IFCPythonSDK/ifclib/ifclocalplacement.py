#!/usr/bin/python
#coding=utf-8
#Filename:IfcLocalPlacement.py
import log
import common
from ifcobjectplacement import IFCOBJECTPLACEMENT

from utils import *

class IFCLOCALPLACEMENT(IFCOBJECTPLACEMENT):
    """"""
    def __init__(self,id,arg):
        super(IFCLOCALPLACEMENT,self).__init__(id,arg)
        self.type='IFCLOCALPLACEMENT'
        self.inverse={}
        self.PlacementRelTo=None #IfcObjectPlacement
        self.RelativePlacement=None #IfcAxis2Placement


    def load(self):
        """register inverses"""
        if not super(IFCLOCALPLACEMENT,self).load():
            return False
        idx=super(IFCLOCALPLACEMENT,self).getAttrCount()
        if self.args.argc()<=idx+0:
            log.error("Inverse links : Error during reading parameter 0 of IfcLocalPlacement, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+0])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 0 of IfcLocalPlacement, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCLOCALPLACEMENT','PlacementRelTo',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCLOCALPLACEMENT,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PlacementRelTo= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelativePlacement= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCLOCALPLACEMENT,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCLOCALPLACEMENT,self).toString()       
        line += idToSPF(self.PlacementRelTo)+','
        line += typerefToSPF(self.RelativePlacement)+','

        return line

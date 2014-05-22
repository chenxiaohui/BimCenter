#!/usr/bin/python
#coding=utf-8
#Filename:IfcMaterialLayerSet.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCMATERIALLAYERSET(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCMATERIALLAYERSET,self).__init__(id,arg)
        self.type='IFCMATERIALLAYERSET'
        self.inverse={}
        self.MaterialLayers=None #LIST
        self.LayerSetName=None #IfcLabel


    def load(self):
        """register inverses"""
        if not super(IFCMATERIALLAYERSET,self).load():
            return False
        idx=super(IFCMATERIALLAYERSET,self).getAttrCount()
        if self.args.argc()<=idx+0:
            log.error("Inverse links : Error during reading parameter 0 of IfcMaterialLayerSet, line %d"%common.counter)
            return False

        currentRefList=getIdListParam(self.args.argv[idx+0])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 0 of IfcMaterialLayerSet, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCMATERIALLAYERSET','MaterialLayers',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCMATERIALLAYERSET,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.MaterialLayers= getIdListParam(arg,spfToId)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.LayerSetName= fromSPF(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCMATERIALLAYERSET,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCMATERIALLAYERSET,self).toString()       
        line += listParamToSPF(self.MaterialLayers,idToSPF)+','
        line += strToSPF(self.LayerSetName)+','

        return line

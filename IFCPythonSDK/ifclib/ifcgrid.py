#!/usr/bin/python
#coding=utf-8
#Filename:IfcGrid.py
import log
import common
from ifcproduct import IFCPRODUCT

from utils import *

class IFCGRID(IFCPRODUCT):
    """"""
    def __init__(self,id,arg):
        super(IFCGRID,self).__init__(id,arg)
        self.type='IFCGRID'
        self.inverse={}
        self.UAxes=None #LIST
        self.VAxes=None #LIST
        self.WAxes=None #LIST
        self.inverse['ContainedInStructure']=[] #inverse:SET of IfcRelContainedInSpatialStructure


    def load(self):
        """register inverses"""
        if not super(IFCGRID,self).load():
            return False
        idx=super(IFCGRID,self).getAttrCount()
        if self.args.argc()<=idx+0:
            log.error("Inverse links : Error during reading parameter 0 of IfcGrid, line %d"%common.counter)
            return False

        currentRefList=getIdListParam(self.args.argv[idx+0])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 0 of IfcGrid, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCGRID','UAxes',self.lid)
        if self.args.argc()<=idx+1:
            log.error("Inverse links : Error during reading parameter 1 of IfcGrid, line %d"%common.counter)
            return False

        currentRefList=getIdListParam(self.args.argv[idx+1])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 1 of IfcGrid, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCGRID','VAxes',self.lid)
        if self.args.argc()<=idx+2:
            log.error("Inverse links : Error during reading parameter 2 of IfcGrid, line %d"%common.counter)
            return False

        currentRefList=getIdListParam(self.args.argv[idx+2])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 2 of IfcGrid, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCGRID','WAxes',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCGRID,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.UAxes= getIdListParam(arg,spfToId)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.VAxes= getIdListParam(arg,spfToId)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.WAxes= getIdListParam(arg,spfToId)

        inverses = self.args.getInverses('IFCRELCONTAINEDINSPATIALSTRUCTURE', 'RelatedElements');
        if inverses:
            self.inverse['ContainedInStructure']=inverses

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCGRID,self).getAttrCount()+3

    def toString(self):
        """"""
        line=super(IFCGRID,self).toString()       
        line += listParamToSPF(self.UAxes,idToSPF)+','
        line += listParamToSPF(self.VAxes,idToSPF)+','
        line += listParamToSPF(self.WAxes,idToSPF)+','

        return line

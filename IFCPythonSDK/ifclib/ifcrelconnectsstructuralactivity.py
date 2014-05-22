#!/usr/bin/python
#coding=utf-8
#Filename:IfcRelConnectsStructuralActivity.py
import log
import common
from ifcrelconnects import IFCRELCONNECTS

from utils import *

class IFCRELCONNECTSSTRUCTURALACTIVITY(IFCRELCONNECTS):
    """"""
    def __init__(self,id,arg):
        super(IFCRELCONNECTSSTRUCTURALACTIVITY,self).__init__(id,arg)
        self.type='IFCRELCONNECTSSTRUCTURALACTIVITY'
        self.inverse={}
        self.RelatingElement=None #IfcStructuralActivityAssignmentSelect
        self.RelatedStructuralActivity=None #IfcStructuralActivity


    def load(self):
        """register inverses"""
        if not super(IFCRELCONNECTSSTRUCTURALACTIVITY,self).load():
            return False
        idx=super(IFCRELCONNECTSSTRUCTURALACTIVITY,self).getAttrCount()
        if self.args.argc()<=idx+0:
            log.error("Inverse links : Error during reading parameter 0 of IfcRelConnectsStructuralActivity, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+0])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 0 of IfcRelConnectsStructuralActivity, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCRELCONNECTSSTRUCTURALACTIVITY','RelatingElement',self.lid)
        if self.args.argc()<=idx+1:
            log.error("Inverse links : Error during reading parameter 1 of IfcRelConnectsStructuralActivity, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+1])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 1 of IfcRelConnectsStructuralActivity, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCRELCONNECTSSTRUCTURALACTIVITY','RelatedStructuralActivity',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCRELCONNECTSSTRUCTURALACTIVITY,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatingElement= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatedStructuralActivity= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCRELCONNECTSSTRUCTURALACTIVITY,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCRELCONNECTSSTRUCTURALACTIVITY,self).toString()       
        line += typerefToSPF(self.RelatingElement)+','
        line += idToSPF(self.RelatedStructuralActivity)+','

        return line

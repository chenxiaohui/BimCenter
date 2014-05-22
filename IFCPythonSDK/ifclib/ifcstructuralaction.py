#!/usr/bin/python
#coding=utf-8
#Filename:IfcStructuralAction.py
import log
import common
from ifcstructuralactivity import IFCSTRUCTURALACTIVITY

from utils import *

class IFCSTRUCTURALACTION(IFCSTRUCTURALACTIVITY):
    """"""
    def __init__(self,id,arg):
        super(IFCSTRUCTURALACTION,self).__init__(id,arg)
        self.type='IFCSTRUCTURALACTION'
        self.inverse={}
        self.DestabilizingLoad=None #BOOLEAN
        self.CausedBy=None #IfcStructuralReaction


    def load(self):
        """register inverses"""
        if not super(IFCSTRUCTURALACTION,self).load():
            return False
        idx=super(IFCSTRUCTURALACTION,self).getAttrCount()
        if self.args.argc()<=idx+1:
            log.error("Inverse links : Error during reading parameter 1 of IfcStructuralAction, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+1])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 1 of IfcStructuralAction, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCSTRUCTURALACTION','CausedBy',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSTRUCTURALACTION,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.DestabilizingLoad= spfToLogical(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.CausedBy= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSTRUCTURALACTION,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCSTRUCTURALACTION,self).toString()       
        line += logicalToSPF(self.DestabilizingLoad)+','
        line += idToSPF(self.CausedBy)+','

        return line

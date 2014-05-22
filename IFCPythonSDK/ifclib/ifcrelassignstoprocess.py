#!/usr/bin/python
#coding=utf-8
#Filename:IfcRelAssignsToProcess.py
import log
import common
from ifcrelassigns import IFCRELASSIGNS

from utils import *

class IFCRELASSIGNSTOPROCESS(IFCRELASSIGNS):
    """"""
    def __init__(self,id,arg):
        super(IFCRELASSIGNSTOPROCESS,self).__init__(id,arg)
        self.type='IFCRELASSIGNSTOPROCESS'
        self.inverse={}
        self.RelatingProcess=None #IfcProcess
        self.QuantityInProcess=None #IfcMeasureWithUnit


    def load(self):
        """register inverses"""
        if not super(IFCRELASSIGNSTOPROCESS,self).load():
            return False
        idx=super(IFCRELASSIGNSTOPROCESS,self).getAttrCount()
        if self.args.argc()<=idx+0:
            log.error("Inverse links : Error during reading parameter 0 of IfcRelAssignsToProcess, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+0])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 0 of IfcRelAssignsToProcess, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCRELASSIGNSTOPROCESS','RelatingProcess',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCRELASSIGNSTOPROCESS,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatingProcess= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.QuantityInProcess= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCRELASSIGNSTOPROCESS,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCRELASSIGNSTOPROCESS,self).toString()       
        line += idToSPF(self.RelatingProcess)+','
        line += idToSPF(self.QuantityInProcess)+','

        return line

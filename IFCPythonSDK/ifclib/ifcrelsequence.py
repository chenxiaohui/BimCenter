#!/usr/bin/python
#coding=utf-8
#Filename:IfcRelSequence.py
import log
import common
from ifcrelconnects import IFCRELCONNECTS

from utils import *

class IFCRELSEQUENCE(IFCRELCONNECTS):
    """"""
    def __init__(self,id,arg):
        super(IFCRELSEQUENCE,self).__init__(id,arg)
        self.type='IFCRELSEQUENCE'
        self.inverse={}
        self.RelatingProcess=None #IfcProcess
        self.RelatedProcess=None #IfcProcess
        self.TimeLag=None #IfcTimeMeasure
        self.SequenceType=None #IfcSequenceEnum


    def load(self):
        """register inverses"""
        if not super(IFCRELSEQUENCE,self).load():
            return False
        idx=super(IFCRELSEQUENCE,self).getAttrCount()
        if self.args.argc()<=idx+0:
            log.error("Inverse links : Error during reading parameter 0 of IfcRelSequence, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+0])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 0 of IfcRelSequence, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCRELSEQUENCE','RelatingProcess',self.lid)
        if self.args.argc()<=idx+1:
            log.error("Inverse links : Error during reading parameter 1 of IfcRelSequence, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+1])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 1 of IfcRelSequence, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCRELSEQUENCE','RelatedProcess',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCRELSEQUENCE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatingProcess= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatedProcess= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.TimeLag= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.SequenceType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCRELSEQUENCE,self).getAttrCount()+4

    def toString(self):
        """"""
        line=super(IFCRELSEQUENCE,self).toString()       
        line += idToSPF(self.RelatingProcess)+','
        line += idToSPF(self.RelatedProcess)+','
        line += integerToSPF(self.TimeLag)+','
        line += typerefToSPF(self.SequenceType)+','

        return line

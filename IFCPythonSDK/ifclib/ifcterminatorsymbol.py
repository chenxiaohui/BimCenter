#!/usr/bin/python
#coding=utf-8
#Filename:IfcTerminatorSymbol.py
import log
import common
from ifcannotationsymboloccurrence import IFCANNOTATIONSYMBOLOCCURRENCE

from utils import *

class IFCTERMINATORSYMBOL(IFCANNOTATIONSYMBOLOCCURRENCE):
    """"""
    def __init__(self,id,arg):
        super(IFCTERMINATORSYMBOL,self).__init__(id,arg)
        self.type='IFCTERMINATORSYMBOL'
        self.inverse={}
        self.AnnotatedCurve=None #IfcAnnotationCurveOccurrence


    def load(self):
        """register inverses"""
        if not super(IFCTERMINATORSYMBOL,self).load():
            return False
        idx=super(IFCTERMINATORSYMBOL,self).getAttrCount()
        if self.args.argc()<=idx+0:
            log.error("Inverse links : Error during reading parameter 0 of IfcTerminatorSymbol, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+0])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 0 of IfcTerminatorSymbol, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCTERMINATORSYMBOL','AnnotatedCurve',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCTERMINATORSYMBOL,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.AnnotatedCurve= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCTERMINATORSYMBOL,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCTERMINATORSYMBOL,self).toString()       
        line += idToSPF(self.AnnotatedCurve)+','

        return line

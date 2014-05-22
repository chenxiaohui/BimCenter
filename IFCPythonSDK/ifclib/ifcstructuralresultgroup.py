#!/usr/bin/python
#coding=utf-8
#Filename:IfcStructuralResultGroup.py
import log
import common
from ifcgroup import IFCGROUP

from utils import *

class IFCSTRUCTURALRESULTGROUP(IFCGROUP):
    """"""
    def __init__(self,id,arg):
        super(IFCSTRUCTURALRESULTGROUP,self).__init__(id,arg)
        self.type='IFCSTRUCTURALRESULTGROUP'
        self.inverse={}
        self.TheoryType=None #IfcAnalysisTheoryTypeEnum
        self.ResultForLoadGroup=None #IfcStructuralLoadGroup
        self.IsLinear=None #BOOLEAN
        self.inverse['ResultGroupFor']=[] #inverse:SET of IfcStructuralAnalysisModel


    def load(self):
        """register inverses"""
        if not super(IFCSTRUCTURALRESULTGROUP,self).load():
            return False
        idx=super(IFCSTRUCTURALRESULTGROUP,self).getAttrCount()
        if self.args.argc()<=idx+1:
            log.error("Inverse links : Error during reading parameter 1 of IfcStructuralResultGroup, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+1])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 1 of IfcStructuralResultGroup, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCSTRUCTURALRESULTGROUP','ResultForLoadGroup',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSTRUCTURALRESULTGROUP,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.TheoryType= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ResultForLoadGroup= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.IsLinear= spfToLogical(arg)

        inverses = self.args.getInverses('IFCSTRUCTURALANALYSISMODEL', 'HasResults');
        if inverses:
            self.inverse['ResultGroupFor']=inverses

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSTRUCTURALRESULTGROUP,self).getAttrCount()+3

    def toString(self):
        """"""
        line=super(IFCSTRUCTURALRESULTGROUP,self).toString()       
        line += typerefToSPF(self.TheoryType)+','
        line += idToSPF(self.ResultForLoadGroup)+','
        line += logicalToSPF(self.IsLinear)+','

        return line

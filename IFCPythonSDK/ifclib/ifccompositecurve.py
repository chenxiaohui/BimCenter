#!/usr/bin/python
#coding=utf-8
#Filename:IfcCompositeCurve.py
import log
import common
from ifcboundedcurve import IFCBOUNDEDCURVE

from utils import *

class IFCCOMPOSITECURVE(IFCBOUNDEDCURVE):
    """"""
    def __init__(self,id,arg):
        super(IFCCOMPOSITECURVE,self).__init__(id,arg)
        self.type='IFCCOMPOSITECURVE'
        self.inverse={}
        self.Segments=None #LIST
        self.SelfIntersect=None #LOGICAL


    def load(self):
        """register inverses"""
        if not super(IFCCOMPOSITECURVE,self).load():
            return False
        idx=super(IFCCOMPOSITECURVE,self).getAttrCount()
        if self.args.argc()<=idx+0:
            log.error("Inverse links : Error during reading parameter 0 of IfcCompositeCurve, line %d"%common.counter)
            return False

        currentRefList=getIdListParam(self.args.argv[idx+0])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 0 of IfcCompositeCurve, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCCOMPOSITECURVE','Segments',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCOMPOSITECURVE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Segments= getIdListParam(arg,spfToId)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.SelfIntersect= spfToLogical(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCOMPOSITECURVE,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCCOMPOSITECURVE,self).toString()       
        line += listParamToSPF(self.Segments,idToSPF)+','
        line += logicalToSPF(self.SelfIntersect)+','

        return line

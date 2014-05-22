#!/usr/bin/python
#coding=utf-8
#Filename:IfcGeometricRepresentationSubContext.py
import log
import common
from ifcgeometricrepresentationcontext import IFCGEOMETRICREPRESENTATIONCONTEXT

from utils import *

class IFCGEOMETRICREPRESENTATIONSUBCONTEXT(IFCGEOMETRICREPRESENTATIONCONTEXT):
    """"""
    def __init__(self,id,arg):
        super(IFCGEOMETRICREPRESENTATIONSUBCONTEXT,self).__init__(id,arg)
        self.type='IFCGEOMETRICREPRESENTATIONSUBCONTEXT'
        self.inverse={}
        self.ParentContext=None #IfcGeometricRepresentationContext
        self.TargetScale=None #IfcPositiveRatioMeasure
        self.TargetView=None #IfcGeometricProjectionEnum
        self.UserDefinedTargetView=None #IfcLabel


    def load(self):
        """register inverses"""
        if not super(IFCGEOMETRICREPRESENTATIONSUBCONTEXT,self).load():
            return False
        idx=super(IFCGEOMETRICREPRESENTATIONSUBCONTEXT,self).getAttrCount()
        if self.args.argc()<=idx+0:
            log.error("Inverse links : Error during reading parameter 0 of IfcGeometricRepresentationSubContext, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+0])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 0 of IfcGeometricRepresentationSubContext, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCGEOMETRICREPRESENTATIONSUBCONTEXT','ParentContext',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCGEOMETRICREPRESENTATIONSUBCONTEXT,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ParentContext= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.TargetScale= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.TargetView= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.UserDefinedTargetView= fromSPF(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCGEOMETRICREPRESENTATIONSUBCONTEXT,self).getAttrCount()+4

    def toString(self):
        """"""
        line=super(IFCGEOMETRICREPRESENTATIONSUBCONTEXT,self).toString()       
        line += idToSPF(self.ParentContext)+','
        line += integerToSPF(self.TargetScale)+','
        line += typerefToSPF(self.TargetView)+','
        line += strToSPF(self.UserDefinedTargetView)+','

        return line

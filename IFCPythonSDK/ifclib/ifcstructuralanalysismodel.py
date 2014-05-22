#!/usr/bin/python
#coding=utf-8
#Filename:IfcStructuralAnalysisModel.py
import log
import common
from ifcsystem import IFCSYSTEM

from utils import *

class IFCSTRUCTURALANALYSISMODEL(IFCSYSTEM):
    """"""
    def __init__(self,id,arg):
        super(IFCSTRUCTURALANALYSISMODEL,self).__init__(id,arg)
        self.type='IFCSTRUCTURALANALYSISMODEL'
        self.inverse={}
        self.PredefinedType=None #IfcAnalysisModelTypeEnum
        self.OrientationOf2DPlane=None #IfcAxis2Placement3D
        self.LoadedBy=None #SET
        self.HasResults=None #SET


    def load(self):
        """register inverses"""
        if not super(IFCSTRUCTURALANALYSISMODEL,self).load():
            return False
        idx=super(IFCSTRUCTURALANALYSISMODEL,self).getAttrCount()
        if self.args.argc()<=idx+2:
            log.error("Inverse links : Error during reading parameter 2 of IfcStructuralAnalysisModel, line %d"%common.counter)
            return False

        currentRefList=getIdListParam(self.args.argv[idx+2])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 2 of IfcStructuralAnalysisModel, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCSTRUCTURALANALYSISMODEL','LoadedBy',self.lid)
        if self.args.argc()<=idx+3:
            log.error("Inverse links : Error during reading parameter 3 of IfcStructuralAnalysisModel, line %d"%common.counter)
            return False

        currentRefList=getIdListParam(self.args.argv[idx+3])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 3 of IfcStructuralAnalysisModel, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCSTRUCTURALANALYSISMODEL','HasResults',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSTRUCTURALANALYSISMODEL,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.OrientationOf2DPlane= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.LoadedBy= getIdListParam(arg,spfToId)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.HasResults= getIdListParam(arg,spfToId)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSTRUCTURALANALYSISMODEL,self).getAttrCount()+4

    def toString(self):
        """"""
        line=super(IFCSTRUCTURALANALYSISMODEL,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','
        line += idToSPF(self.OrientationOf2DPlane)+','
        line += listParamToSPF(self.LoadedBy,idToSPF)+','
        line += listParamToSPF(self.HasResults,idToSPF)+','

        return line

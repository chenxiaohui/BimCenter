#!/usr/bin/python
#coding=utf-8
#Filename:IfcRelConnectsStructuralElement.py
import log
import common
from ifcrelconnects import IFCRELCONNECTS

from utils import *

class IFCRELCONNECTSSTRUCTURALELEMENT(IFCRELCONNECTS):
    """"""
    def __init__(self,id,arg):
        super(IFCRELCONNECTSSTRUCTURALELEMENT,self).__init__(id,arg)
        self.type='IFCRELCONNECTSSTRUCTURALELEMENT'
        self.inverse={}
        self.RelatingElement=None #IfcElement
        self.RelatedStructuralMember=None #IfcStructuralMember


    def load(self):
        """register inverses"""
        if not super(IFCRELCONNECTSSTRUCTURALELEMENT,self).load():
            return False
        idx=super(IFCRELCONNECTSSTRUCTURALELEMENT,self).getAttrCount()
        if self.args.argc()<=idx+0:
            log.error("Inverse links : Error during reading parameter 0 of IfcRelConnectsStructuralElement, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+0])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 0 of IfcRelConnectsStructuralElement, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCRELCONNECTSSTRUCTURALELEMENT','RelatingElement',self.lid)
        if self.args.argc()<=idx+1:
            log.error("Inverse links : Error during reading parameter 1 of IfcRelConnectsStructuralElement, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+1])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 1 of IfcRelConnectsStructuralElement, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCRELCONNECTSSTRUCTURALELEMENT','RelatedStructuralMember',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCRELCONNECTSSTRUCTURALELEMENT,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatingElement= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatedStructuralMember= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCRELCONNECTSSTRUCTURALELEMENT,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCRELCONNECTSSTRUCTURALELEMENT,self).toString()       
        line += idToSPF(self.RelatingElement)+','
        line += idToSPF(self.RelatedStructuralMember)+','

        return line

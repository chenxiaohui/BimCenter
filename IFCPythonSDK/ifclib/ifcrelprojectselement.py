#!/usr/bin/python
#coding=utf-8
#Filename:IfcRelProjectsElement.py
import log
import common
from ifcrelconnects import IFCRELCONNECTS

from utils import *

class IFCRELPROJECTSELEMENT(IFCRELCONNECTS):
    """"""
    def __init__(self,id,arg):
        super(IFCRELPROJECTSELEMENT,self).__init__(id,arg)
        self.type='IFCRELPROJECTSELEMENT'
        self.inverse={}
        self.RelatingElement=None #IfcElement
        self.RelatedFeatureElement=None #IfcFeatureElementAddition


    def load(self):
        """register inverses"""
        if not super(IFCRELPROJECTSELEMENT,self).load():
            return False
        idx=super(IFCRELPROJECTSELEMENT,self).getAttrCount()
        if self.args.argc()<=idx+0:
            log.error("Inverse links : Error during reading parameter 0 of IfcRelProjectsElement, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+0])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 0 of IfcRelProjectsElement, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCRELPROJECTSELEMENT','RelatingElement',self.lid)
        if self.args.argc()<=idx+1:
            log.error("Inverse links : Error during reading parameter 1 of IfcRelProjectsElement, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+1])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 1 of IfcRelProjectsElement, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCRELPROJECTSELEMENT','RelatedFeatureElement',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCRELPROJECTSELEMENT,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatingElement= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatedFeatureElement= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCRELPROJECTSELEMENT,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCRELPROJECTSELEMENT,self).toString()       
        line += idToSPF(self.RelatingElement)+','
        line += idToSPF(self.RelatedFeatureElement)+','

        return line

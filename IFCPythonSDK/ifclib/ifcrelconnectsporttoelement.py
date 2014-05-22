#!/usr/bin/python
#coding=utf-8
#Filename:IfcRelConnectsPortToElement.py
import log
import common
from ifcrelconnects import IFCRELCONNECTS

from utils import *

class IFCRELCONNECTSPORTTOELEMENT(IFCRELCONNECTS):
    """"""
    def __init__(self,id,arg):
        super(IFCRELCONNECTSPORTTOELEMENT,self).__init__(id,arg)
        self.type='IFCRELCONNECTSPORTTOELEMENT'
        self.inverse={}
        self.RelatingPort=None #IfcPort
        self.RelatedElement=None #IfcElement


    def load(self):
        """register inverses"""
        if not super(IFCRELCONNECTSPORTTOELEMENT,self).load():
            return False
        idx=super(IFCRELCONNECTSPORTTOELEMENT,self).getAttrCount()
        if self.args.argc()<=idx+0:
            log.error("Inverse links : Error during reading parameter 0 of IfcRelConnectsPortToElement, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+0])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 0 of IfcRelConnectsPortToElement, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCRELCONNECTSPORTTOELEMENT','RelatingPort',self.lid)
        if self.args.argc()<=idx+1:
            log.error("Inverse links : Error during reading parameter 1 of IfcRelConnectsPortToElement, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+1])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 1 of IfcRelConnectsPortToElement, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCRELCONNECTSPORTTOELEMENT','RelatedElement',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCRELCONNECTSPORTTOELEMENT,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatingPort= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatedElement= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCRELCONNECTSPORTTOELEMENT,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCRELCONNECTSPORTTOELEMENT,self).toString()       
        line += idToSPF(self.RelatingPort)+','
        line += idToSPF(self.RelatedElement)+','

        return line

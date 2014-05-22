#!/usr/bin/python
#coding=utf-8
#Filename:IfcRelAssignsToResource.py
import log
import common
from ifcrelassigns import IFCRELASSIGNS

from utils import *

class IFCRELASSIGNSTORESOURCE(IFCRELASSIGNS):
    """"""
    def __init__(self,id,arg):
        super(IFCRELASSIGNSTORESOURCE,self).__init__(id,arg)
        self.type='IFCRELASSIGNSTORESOURCE'
        self.inverse={}
        self.RelatingResource=None #IfcResource


    def load(self):
        """register inverses"""
        if not super(IFCRELASSIGNSTORESOURCE,self).load():
            return False
        idx=super(IFCRELASSIGNSTORESOURCE,self).getAttrCount()
        if self.args.argc()<=idx+0:
            log.error("Inverse links : Error during reading parameter 0 of IfcRelAssignsToResource, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+0])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 0 of IfcRelAssignsToResource, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCRELASSIGNSTORESOURCE','RelatingResource',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCRELASSIGNSTORESOURCE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatingResource= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCRELASSIGNSTORESOURCE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCRELASSIGNSTORESOURCE,self).toString()       
        line += idToSPF(self.RelatingResource)+','

        return line

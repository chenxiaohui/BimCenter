#!/usr/bin/python
#coding=utf-8
#Filename:IfcRelAssignsToActor.py
import log
import common
from ifcrelassigns import IFCRELASSIGNS

from utils import *

class IFCRELASSIGNSTOACTOR(IFCRELASSIGNS):
    """"""
    def __init__(self,id,arg):
        super(IFCRELASSIGNSTOACTOR,self).__init__(id,arg)
        self.type='IFCRELASSIGNSTOACTOR'
        self.inverse={}
        self.RelatingActor=None #IfcActor
        self.ActingRole=None #IfcActorRole


    def load(self):
        """register inverses"""
        if not super(IFCRELASSIGNSTOACTOR,self).load():
            return False
        idx=super(IFCRELASSIGNSTOACTOR,self).getAttrCount()
        if self.args.argc()<=idx+0:
            log.error("Inverse links : Error during reading parameter 0 of IfcRelAssignsToActor, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+0])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 0 of IfcRelAssignsToActor, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCRELASSIGNSTOACTOR','RelatingActor',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCRELASSIGNSTOACTOR,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatingActor= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ActingRole= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCRELASSIGNSTOACTOR,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCRELASSIGNSTOACTOR,self).toString()       
        line += idToSPF(self.RelatingActor)+','
        line += idToSPF(self.ActingRole)+','

        return line

#!/usr/bin/python
#coding=utf-8
#Filename:IfcRelDefinesByType.py
import log
import common
from ifcreldefines import IFCRELDEFINES

from utils import *

class IFCRELDEFINESBYTYPE(IFCRELDEFINES):
    """"""
    def __init__(self,id,arg):
        super(IFCRELDEFINESBYTYPE,self).__init__(id,arg)
        self.type='IFCRELDEFINESBYTYPE'
        self.inverse={}
        self.RelatingType=None #IfcTypeObject


    def load(self):
        """register inverses"""
        if not super(IFCRELDEFINESBYTYPE,self).load():
            return False
        idx=super(IFCRELDEFINESBYTYPE,self).getAttrCount()
        if self.args.argc()<=idx+0:
            log.error("Inverse links : Error during reading parameter 0 of IfcRelDefinesByType, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+0])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 0 of IfcRelDefinesByType, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCRELDEFINESBYTYPE','RelatingType',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCRELDEFINESBYTYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatingType= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCRELDEFINESBYTYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCRELDEFINESBYTYPE,self).toString()       
        line += idToSPF(self.RelatingType)+','

        return line

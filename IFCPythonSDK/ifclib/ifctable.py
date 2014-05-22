#!/usr/bin/python
#coding=utf-8
#Filename:IfcTable.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCTABLE(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCTABLE,self).__init__(id,arg)
        self.type='IFCTABLE'
        self.inverse={}
        self.Name=None #STRING
        self.Rows=None #LIST


    def load(self):
        """register inverses"""
        if not super(IFCTABLE,self).load():
            return False
        idx=super(IFCTABLE,self).getAttrCount()
        if self.args.argc()<=idx+1:
            log.error("Inverse links : Error during reading parameter 1 of IfcTable, line %d"%common.counter)
            return False

        currentRefList=getIdListParam(self.args.argv[idx+1])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 1 of IfcTable, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCTABLE','Rows',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCTABLE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Name= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Rows= getIdListParam(arg,spfToId)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCTABLE,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCTABLE,self).toString()       
        line += strToSPF(self.Name)+','
        line += listParamToSPF(self.Rows,idToSPF)+','

        return line

#!/usr/bin/python
#coding=utf-8
#Filename:IfcRelAssignsToGroup.py
import log
import common
from ifcrelassigns import IFCRELASSIGNS

from utils import *

class IFCRELASSIGNSTOGROUP(IFCRELASSIGNS):
    """"""
    def __init__(self,id,arg):
        super(IFCRELASSIGNSTOGROUP,self).__init__(id,arg)
        self.type='IFCRELASSIGNSTOGROUP'
        self.inverse={}
        self.RelatingGroup=None #IfcGroup


    def load(self):
        """register inverses"""
        if not super(IFCRELASSIGNSTOGROUP,self).load():
            return False
        idx=super(IFCRELASSIGNSTOGROUP,self).getAttrCount()
        if self.args.argc()<=idx+0:
            log.error("Inverse links : Error during reading parameter 0 of IfcRelAssignsToGroup, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+0])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 0 of IfcRelAssignsToGroup, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCRELASSIGNSTOGROUP','RelatingGroup',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCRELASSIGNSTOGROUP,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatingGroup= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCRELASSIGNSTOGROUP,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCRELASSIGNSTOGROUP,self).toString()       
        line += idToSPF(self.RelatingGroup)+','

        return line

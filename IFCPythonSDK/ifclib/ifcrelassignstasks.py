#!/usr/bin/python
#coding=utf-8
#Filename:IfcRelAssignsTasks.py
import log
import common
from ifcrelassignstocontrol import IFCRELASSIGNSTOCONTROL

from utils import *

class IFCRELASSIGNSTASKS(IFCRELASSIGNSTOCONTROL):
    """"""
    def __init__(self,id,arg):
        super(IFCRELASSIGNSTASKS,self).__init__(id,arg)
        self.type='IFCRELASSIGNSTASKS'
        self.inverse={}
        self.TimeForTask=None #IfcScheduleTimeControl


    def load(self):
        """register inverses"""
        if not super(IFCRELASSIGNSTASKS,self).load():
            return False
        idx=super(IFCRELASSIGNSTASKS,self).getAttrCount()
        if self.args.argc()<=idx+0:
            log.error("Inverse links : Error during reading parameter 0 of IfcRelAssignsTasks, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+0])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 0 of IfcRelAssignsTasks, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCRELASSIGNSTASKS','TimeForTask',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCRELASSIGNSTASKS,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.TimeForTask= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCRELASSIGNSTASKS,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCRELASSIGNSTASKS,self).toString()       
        line += idToSPF(self.TimeForTask)+','

        return line

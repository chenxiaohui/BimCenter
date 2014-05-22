#!/usr/bin/python
#coding=utf-8
#Filename:IfcRelAssignsToControl.py
import log
import common
from ifcrelassigns import IFCRELASSIGNS

from utils import *

class IFCRELASSIGNSTOCONTROL(IFCRELASSIGNS):
    """"""
    def __init__(self,id,arg):
        super(IFCRELASSIGNSTOCONTROL,self).__init__(id,arg)
        self.type='IFCRELASSIGNSTOCONTROL'
        self.inverse={}
        self.RelatingControl=None #IfcControl


    def load(self):
        """register inverses"""
        if not super(IFCRELASSIGNSTOCONTROL,self).load():
            return False
        idx=super(IFCRELASSIGNSTOCONTROL,self).getAttrCount()
        if self.args.argc()<=idx+0:
            log.error("Inverse links : Error during reading parameter 0 of IfcRelAssignsToControl, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+0])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 0 of IfcRelAssignsToControl, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCRELASSIGNSTOCONTROL','RelatingControl',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCRELASSIGNSTOCONTROL,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatingControl= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCRELASSIGNSTOCONTROL,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCRELASSIGNSTOCONTROL,self).toString()       
        line += idToSPF(self.RelatingControl)+','

        return line

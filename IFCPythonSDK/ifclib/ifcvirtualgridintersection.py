#!/usr/bin/python
#coding=utf-8
#Filename:IfcVirtualGridIntersection.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCVIRTUALGRIDINTERSECTION(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCVIRTUALGRIDINTERSECTION,self).__init__(id,arg)
        self.type='IFCVIRTUALGRIDINTERSECTION'
        self.inverse={}
        self.IntersectingAxes=None #LIST
        self.OffsetDistances=None #LIST


    def load(self):
        """register inverses"""
        if not super(IFCVIRTUALGRIDINTERSECTION,self).load():
            return False
        idx=super(IFCVIRTUALGRIDINTERSECTION,self).getAttrCount()
        if self.args.argc()<=idx+0:
            log.error("Inverse links : Error during reading parameter 0 of IfcVirtualGridIntersection, line %d"%common.counter)
            return False

        currentRefList=getIdListParam(self.args.argv[idx+0])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 0 of IfcVirtualGridIntersection, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCVIRTUALGRIDINTERSECTION','IntersectingAxes',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCVIRTUALGRIDINTERSECTION,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.IntersectingAxes= getIdListParam(arg,spfToId)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.OffsetDistances= getIdListParam(arg,spfToInteger)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCVIRTUALGRIDINTERSECTION,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCVIRTUALGRIDINTERSECTION,self).toString()       
        line += listParamToSPF(self.IntersectingAxes,idToSPF)+','
        line += listParamToSPF(self.OffsetDistances,integerToSPF)+','

        return line

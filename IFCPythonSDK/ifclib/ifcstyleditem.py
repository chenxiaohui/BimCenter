#!/usr/bin/python
#coding=utf-8
#Filename:IfcStyledItem.py
import log
import common
from ifcrepresentationitem import IFCREPRESENTATIONITEM

from utils import *

class IFCSTYLEDITEM(IFCREPRESENTATIONITEM):
    """"""
    def __init__(self,id,arg):
        super(IFCSTYLEDITEM,self).__init__(id,arg)
        self.type='IFCSTYLEDITEM'
        self.inverse={}
        self.Item=None #IfcRepresentationItem
        self.Styles=None #SET
        self.Name=None #IfcLabel


    def load(self):
        """register inverses"""
        if not super(IFCSTYLEDITEM,self).load():
            return False
        idx=super(IFCSTYLEDITEM,self).getAttrCount()
        if self.args.argc()<=idx+0:
            log.error("Inverse links : Error during reading parameter 0 of IfcStyledItem, line %d"%common.counter)
            return False

        currentRefList=getIdParam(self.args.argv[idx+0])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter 0 of IfcStyledItem, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('IFCSTYLEDITEM','Item',self.lid)

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSTYLEDITEM,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Item= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Styles= getIdListParam(arg,spfToId)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Name= fromSPF(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSTYLEDITEM,self).getAttrCount()+3

    def toString(self):
        """"""
        line=super(IFCSTYLEDITEM,self).toString()       
        line += idToSPF(self.Item)+','
        line += listParamToSPF(self.Styles,idToSPF)+','
        line += strToSPF(self.Name)+','

        return line

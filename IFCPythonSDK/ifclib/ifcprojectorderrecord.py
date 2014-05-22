#!/usr/bin/python
#coding=utf-8
#Filename:IfcProjectOrderRecord.py
import log
import common
from ifccontrol import IFCCONTROL

from utils import *

class IFCPROJECTORDERRECORD(IFCCONTROL):
    """"""
    def __init__(self,id,arg):
        super(IFCPROJECTORDERRECORD,self).__init__(id,arg)
        self.type='IFCPROJECTORDERRECORD'
        self.inverse={}
        self.Records=None #LIST
        self.PredefinedType=None #IfcProjectOrderRecordTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCPROJECTORDERRECORD,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCPROJECTORDERRECORD,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Records= getIdListParam(arg,spfToId)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCPROJECTORDERRECORD,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCPROJECTORDERRECORD,self).toString()       
        line += listParamToSPF(self.Records,idToSPF)+','
        line += typerefToSPF(self.PredefinedType)+','

        return line

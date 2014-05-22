#!/usr/bin/python
#coding=utf-8
#Filename:IfcDuctSilencerType.py
import log
import common
from ifcflowtreatmentdevicetype import IFCFLOWTREATMENTDEVICETYPE

from utils import *

class IFCDUCTSILENCERTYPE(IFCFLOWTREATMENTDEVICETYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCDUCTSILENCERTYPE,self).__init__(id,arg)
        self.type='IFCDUCTSILENCERTYPE'
        self.inverse={}
        self.PredefinedType=None #IfcDuctSilencerTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCDUCTSILENCERTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCDUCTSILENCERTYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCDUCTSILENCERTYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCDUCTSILENCERTYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line

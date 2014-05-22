#!/usr/bin/python
#coding=utf-8
#Filename:IfcClassificationReference.py
import log
import common
from ifcexternalreference import IFCEXTERNALREFERENCE

from utils import *

class IFCCLASSIFICATIONREFERENCE(IFCEXTERNALREFERENCE):
    """"""
    def __init__(self,id,arg):
        super(IFCCLASSIFICATIONREFERENCE,self).__init__(id,arg)
        self.type='IFCCLASSIFICATIONREFERENCE'
        self.inverse={}
        self.ReferencedSource=None #IfcClassification


    def load(self):
        """register inverses"""
        if not super(IFCCLASSIFICATIONREFERENCE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCLASSIFICATIONREFERENCE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ReferencedSource= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCLASSIFICATIONREFERENCE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCCLASSIFICATIONREFERENCE,self).toString()       
        line += idToSPF(self.ReferencedSource)+','

        return line

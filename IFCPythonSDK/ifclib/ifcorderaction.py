#!/usr/bin/python
#coding=utf-8
#Filename:IfcOrderAction.py
import log
import common
from ifctask import IFCTASK

from utils import *

class IFCORDERACTION(IFCTASK):
    """"""
    def __init__(self,id,arg):
        super(IFCORDERACTION,self).__init__(id,arg)
        self.type='IFCORDERACTION'
        self.inverse={}
        self.ActionID=None #IfcIdentifier


    def load(self):
        """register inverses"""
        if not super(IFCORDERACTION,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCORDERACTION,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ActionID= fromSPF(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCORDERACTION,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCORDERACTION,self).toString()       
        line += strToSPF(self.ActionID)+','

        return line

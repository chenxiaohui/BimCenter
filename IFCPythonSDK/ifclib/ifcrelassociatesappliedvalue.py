#!/usr/bin/python
#coding=utf-8
#Filename:IfcRelAssociatesAppliedValue.py
import log
import common
from ifcrelassociates import IFCRELASSOCIATES

from utils import *

class IFCRELASSOCIATESAPPLIEDVALUE(IFCRELASSOCIATES):
    """"""
    def __init__(self,id,arg):
        super(IFCRELASSOCIATESAPPLIEDVALUE,self).__init__(id,arg)
        self.type='IFCRELASSOCIATESAPPLIEDVALUE'
        self.inverse={}
        self.RelatingAppliedValue=None #IfcAppliedValue


    def load(self):
        """register inverses"""
        if not super(IFCRELASSOCIATESAPPLIEDVALUE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCRELASSOCIATESAPPLIEDVALUE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatingAppliedValue= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCRELASSOCIATESAPPLIEDVALUE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCRELASSOCIATESAPPLIEDVALUE,self).toString()       
        line += idToSPF(self.RelatingAppliedValue)+','

        return line

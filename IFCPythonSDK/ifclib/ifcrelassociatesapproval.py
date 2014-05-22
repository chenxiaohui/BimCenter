#!/usr/bin/python
#coding=utf-8
#Filename:IfcRelAssociatesApproval.py
import log
import common
from ifcrelassociates import IFCRELASSOCIATES

from utils import *

class IFCRELASSOCIATESAPPROVAL(IFCRELASSOCIATES):
    """"""
    def __init__(self,id,arg):
        super(IFCRELASSOCIATESAPPROVAL,self).__init__(id,arg)
        self.type='IFCRELASSOCIATESAPPROVAL'
        self.inverse={}
        self.RelatingApproval=None #IfcApproval


    def load(self):
        """register inverses"""
        if not super(IFCRELASSOCIATESAPPROVAL,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCRELASSOCIATESAPPROVAL,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatingApproval= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCRELASSOCIATESAPPROVAL,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCRELASSOCIATESAPPROVAL,self).toString()       
        line += idToSPF(self.RelatingApproval)+','

        return line

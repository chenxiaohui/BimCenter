#!/usr/bin/python
#coding=utf-8
#Filename:IfcPermit.py
import log
import common
from ifccontrol import IFCCONTROL

from utils import *

class IFCPERMIT(IFCCONTROL):
    """"""
    def __init__(self,id,arg):
        super(IFCPERMIT,self).__init__(id,arg)
        self.type='IFCPERMIT'
        self.inverse={}
        self.PermitID=None #IfcIdentifier


    def load(self):
        """register inverses"""
        if not super(IFCPERMIT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCPERMIT,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PermitID= fromSPF(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCPERMIT,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCPERMIT,self).toString()       
        line += strToSPF(self.PermitID)+','

        return line

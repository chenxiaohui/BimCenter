#!/usr/bin/python
#coding=utf-8
#Filename:IfcActionRequest.py
import log
import common
from ifccontrol import IFCCONTROL

from utils import *

class IFCACTIONREQUEST(IFCCONTROL):
    """"""
    def __init__(self,id,arg):
        super(IFCACTIONREQUEST,self).__init__(id,arg)
        self.type='IFCACTIONREQUEST'
        self.inverse={}
        self.RequestID=None #IfcIdentifier


    def load(self):
        """register inverses"""
        if not super(IFCACTIONREQUEST,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCACTIONREQUEST,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RequestID= fromSPF(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCACTIONREQUEST,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCACTIONREQUEST,self).toString()       
        line += strToSPF(self.RequestID)+','

        return line

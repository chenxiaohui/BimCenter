#!/usr/bin/python
#coding=utf-8
#Filename:IfcExternalReference.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCEXTERNALREFERENCE(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCEXTERNALREFERENCE,self).__init__(id,arg)
        self.type='IFCEXTERNALREFERENCE'
        self.inverse={}
        self.Location=None #IfcLabel
        self.ItemReference=None #IfcIdentifier
        self.Name=None #IfcLabel


    def load(self):
        """register inverses"""
        if not super(IFCEXTERNALREFERENCE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCEXTERNALREFERENCE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Location= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ItemReference= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Name= fromSPF(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCEXTERNALREFERENCE,self).getAttrCount()+3

    def toString(self):
        """"""
        line=super(IFCEXTERNALREFERENCE,self).toString()       
        line += strToSPF(self.Location)+','
        line += strToSPF(self.ItemReference)+','
        line += strToSPF(self.Name)+','

        return line

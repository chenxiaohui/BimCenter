#!/usr/bin/python
#coding=utf-8
#Filename:IfcRoot.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCROOT(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCROOT,self).__init__(id,arg)
        self.type='IFCROOT'
        self.inverse={}
        self.GlobalId=None #IfcGloballyUniqueId
        self.OwnerHistory=None #IfcOwnerHistory
        self.Name=None #IfcLabel
        self.Description=None #IfcText


    def load(self):
        """register inverses"""
        if not super(IFCROOT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCROOT,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.GlobalId= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.OwnerHistory= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Name= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Description= fromSPF(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCROOT,self).getAttrCount()+4

    def toString(self):
        """"""
        line=super(IFCROOT,self).toString()       
        line += strToSPF(self.GlobalId)+','
        line += idToSPF(self.OwnerHistory)+','
        line += strToSPF(self.Name)+','
        line += strToSPF(self.Description)+','

        return line

#!/usr/bin/python
#coding=utf-8
#Filename:IfcActorRole.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCACTORROLE(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCACTORROLE,self).__init__(id,arg)
        self.type='IFCACTORROLE'
        self.inverse={}
        self.Role=None #IfcRoleEnum
        self.UserDefinedRole=None #IfcLabel
        self.Description=None #IfcText


    def load(self):
        """register inverses"""
        if not super(IFCACTORROLE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCACTORROLE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Role= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.UserDefinedRole= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Description= fromSPF(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCACTORROLE,self).getAttrCount()+3

    def toString(self):
        """"""
        line=super(IFCACTORROLE,self).toString()       
        line += typerefToSPF(self.Role)+','
        line += strToSPF(self.UserDefinedRole)+','
        line += strToSPF(self.Description)+','

        return line

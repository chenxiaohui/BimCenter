#!/usr/bin/python
#coding=utf-8
#Filename:IfcPreDefinedItem.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCPREDEFINEDITEM(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCPREDEFINEDITEM,self).__init__(id,arg)
        self.type='IFCPREDEFINEDITEM'
        self.inverse={}
        self.Name=None #IfcLabel


    def load(self):
        """register inverses"""
        if not super(IFCPREDEFINEDITEM,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCPREDEFINEDITEM,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Name= fromSPF(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCPREDEFINEDITEM,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCPREDEFINEDITEM,self).toString()       
        line += strToSPF(self.Name)+','

        return line

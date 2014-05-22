#!/usr/bin/python
#coding=utf-8
#Filename:IfcProjectOrder.py
import log
import common
from ifccontrol import IFCCONTROL

from utils import *

class IFCPROJECTORDER(IFCCONTROL):
    """"""
    def __init__(self,id,arg):
        super(IFCPROJECTORDER,self).__init__(id,arg)
        self.type='IFCPROJECTORDER'
        self.inverse={}
        self.ID=None #IfcIdentifier
        self.PredefinedType=None #IfcProjectOrderTypeEnum
        self.Status=None #IfcLabel


    def load(self):
        """register inverses"""
        if not super(IFCPROJECTORDER,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCPROJECTORDER,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ID= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Status= fromSPF(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCPROJECTORDER,self).getAttrCount()+3

    def toString(self):
        """"""
        line=super(IFCPROJECTORDER,self).toString()       
        line += strToSPF(self.ID)+','
        line += typerefToSPF(self.PredefinedType)+','
        line += strToSPF(self.Status)+','

        return line

#!/usr/bin/python
#coding=utf-8
#Filename:IfcPropertyReferenceValue.py
import log
import common
from ifcsimpleproperty import IFCSIMPLEPROPERTY

from utils import *

class IFCPROPERTYREFERENCEVALUE(IFCSIMPLEPROPERTY):
    """"""
    def __init__(self,id,arg):
        super(IFCPROPERTYREFERENCEVALUE,self).__init__(id,arg)
        self.type='IFCPROPERTYREFERENCEVALUE'
        self.inverse={}
        self.UsageName=None #IfcLabel
        self.PropertyReference=None #IfcObjectReferenceSelect


    def load(self):
        """register inverses"""
        if not super(IFCPROPERTYREFERENCEVALUE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCPROPERTYREFERENCEVALUE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.UsageName= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PropertyReference= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCPROPERTYREFERENCEVALUE,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCPROPERTYREFERENCEVALUE,self).toString()       
        line += strToSPF(self.UsageName)+','
        line += typerefToSPF(self.PropertyReference)+','

        return line

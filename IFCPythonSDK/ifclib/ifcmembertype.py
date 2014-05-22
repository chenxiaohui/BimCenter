#!/usr/bin/python
#coding=utf-8
#Filename:IfcMemberType.py
import log
import common
from ifcbuildingelementtype import IFCBUILDINGELEMENTTYPE

from utils import *

class IFCMEMBERTYPE(IFCBUILDINGELEMENTTYPE):
    """"""
    def __init__(self,id,arg):
        super(IFCMEMBERTYPE,self).__init__(id,arg)
        self.type='IFCMEMBERTYPE'
        self.inverse={}
        self.PredefinedType=None #IfcMemberTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCMEMBERTYPE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCMEMBERTYPE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCMEMBERTYPE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCMEMBERTYPE,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line

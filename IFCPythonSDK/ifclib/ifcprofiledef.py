#!/usr/bin/python
#coding=utf-8
#Filename:IfcProfileDef.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCPROFILEDEF(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCPROFILEDEF,self).__init__(id,arg)
        self.type='IFCPROFILEDEF'
        self.inverse={}
        self.ProfileType=None #IfcProfileTypeEnum
        self.ProfileName=None #IfcLabel


    def load(self):
        """register inverses"""
        if not super(IFCPROFILEDEF,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCPROFILEDEF,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ProfileType= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ProfileName= fromSPF(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCPROFILEDEF,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCPROFILEDEF,self).toString()       
        line += typerefToSPF(self.ProfileType)+','
        line += strToSPF(self.ProfileName)+','

        return line

#!/usr/bin/python
#coding=utf-8
#Filename:IfcProfileProperties.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCPROFILEPROPERTIES(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCPROFILEPROPERTIES,self).__init__(id,arg)
        self.type='IFCPROFILEPROPERTIES'
        self.inverse={}
        self.ProfileName=None #IfcLabel
        self.ProfileDefinition=None #IfcProfileDef


    def load(self):
        """register inverses"""
        if not super(IFCPROFILEPROPERTIES,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCPROFILEPROPERTIES,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ProfileName= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ProfileDefinition= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCPROFILEPROPERTIES,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCPROFILEPROPERTIES,self).toString()       
        line += strToSPF(self.ProfileName)+','
        line += idToSPF(self.ProfileDefinition)+','

        return line

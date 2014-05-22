#!/usr/bin/python
#coding=utf-8
#Filename:IfcApplication.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCAPPLICATION(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCAPPLICATION,self).__init__(id,arg)
        self.type='IFCAPPLICATION'
        self.inverse={}
        self.ApplicationDeveloper=None #IfcOrganization
        self.Version=None #IfcLabel
        self.ApplicationFullName=None #IfcLabel
        self.ApplicationIdentifier=None #IfcIdentifier


    def load(self):
        """register inverses"""
        if not super(IFCAPPLICATION,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCAPPLICATION,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ApplicationDeveloper= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Version= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ApplicationFullName= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ApplicationIdentifier= fromSPF(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCAPPLICATION,self).getAttrCount()+4

    def toString(self):
        """"""
        line=super(IFCAPPLICATION,self).toString()       
        line += idToSPF(self.ApplicationDeveloper)+','
        line += strToSPF(self.Version)+','
        line += strToSPF(self.ApplicationFullName)+','
        line += strToSPF(self.ApplicationIdentifier)+','

        return line

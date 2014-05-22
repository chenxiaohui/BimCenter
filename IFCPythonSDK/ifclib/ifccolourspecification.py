#!/usr/bin/python
#coding=utf-8
#Filename:IfcColourSpecification.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCCOLOURSPECIFICATION(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCCOLOURSPECIFICATION,self).__init__(id,arg)
        self.type='IFCCOLOURSPECIFICATION'
        self.inverse={}
        self.Name=None #IfcLabel


    def load(self):
        """register inverses"""
        if not super(IFCCOLOURSPECIFICATION,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCOLOURSPECIFICATION,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Name= fromSPF(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCOLOURSPECIFICATION,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCCOLOURSPECIFICATION,self).toString()       
        line += strToSPF(self.Name)+','

        return line

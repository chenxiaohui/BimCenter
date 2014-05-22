#!/usr/bin/python
#coding=utf-8
#Filename:IfcPresentationStyleAssignment.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCPRESENTATIONSTYLEASSIGNMENT(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCPRESENTATIONSTYLEASSIGNMENT,self).__init__(id,arg)
        self.type='IFCPRESENTATIONSTYLEASSIGNMENT'
        self.inverse={}
        self.Styles=None #SET


    def load(self):
        """register inverses"""
        if not super(IFCPRESENTATIONSTYLEASSIGNMENT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCPRESENTATIONSTYLEASSIGNMENT,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Styles= getIdListParam(arg,spfToTypeRef)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCPRESENTATIONSTYLEASSIGNMENT,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCPRESENTATIONSTYLEASSIGNMENT,self).toString()       
        line += listParamToSPF(self.Styles,typerefToSPF)+','

        return line

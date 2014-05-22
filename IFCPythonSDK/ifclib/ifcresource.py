#!/usr/bin/python
#coding=utf-8
#Filename:IfcResource.py
import log
import common
from ifcobject import IFCOBJECT

from utils import *

class IFCRESOURCE(IFCOBJECT):
    """"""
    def __init__(self,id,arg):
        super(IFCRESOURCE,self).__init__(id,arg)
        self.type='IFCRESOURCE'
        self.inverse={}
        self.inverse['ResourceOf']=[] #inverse:SET of IfcRelAssignsToResource


    def load(self):
        """register inverses"""
        if not super(IFCRESOURCE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCRESOURCE,self).init():
            return False

        inverses = self.args.getInverses('IFCRELASSIGNSTORESOURCE', 'RelatingResource');
        if inverses:
            self.inverse['ResourceOf']=inverses

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCRESOURCE,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCRESOURCE,self).toString()       

        return line

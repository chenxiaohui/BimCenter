#!/usr/bin/python
#coding=utf-8
#Filename:IfcSystem.py
import log
import common
from ifcgroup import IFCGROUP

from utils import *

class IFCSYSTEM(IFCGROUP):
    """"""
    def __init__(self,id,arg):
        super(IFCSYSTEM,self).__init__(id,arg)
        self.type='IFCSYSTEM'
        self.inverse={}
        self.inverse['ServicesBuildings']=[] #inverse:SET of IfcRelServicesBuildings


    def load(self):
        """register inverses"""
        if not super(IFCSYSTEM,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSYSTEM,self).init():
            return False

        inverses = self.args.getInverses('IFCRELSERVICESBUILDINGS', 'RelatingSystem');
        if inverses:
            self.inverse['ServicesBuildings']=inverses

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSYSTEM,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCSYSTEM,self).toString()       

        return line

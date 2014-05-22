#!/usr/bin/python
#coding=utf-8
#Filename:IfcServiceLife.py
import log
import common
from ifccontrol import IFCCONTROL

from utils import *

class IFCSERVICELIFE(IFCCONTROL):
    """"""
    def __init__(self,id,arg):
        super(IFCSERVICELIFE,self).__init__(id,arg)
        self.type='IFCSERVICELIFE'
        self.inverse={}
        self.ServiceLifeType=None #IfcServiceLifeTypeEnum
        self.ServiceLifeDuration=None #IfcTimeMeasure


    def load(self):
        """register inverses"""
        if not super(IFCSERVICELIFE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSERVICELIFE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ServiceLifeType= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ServiceLifeDuration= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSERVICELIFE,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCSERVICELIFE,self).toString()       
        line += typerefToSPF(self.ServiceLifeType)+','
        line += integerToSPF(self.ServiceLifeDuration)+','

        return line

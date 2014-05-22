#!/usr/bin/python
#coding=utf-8
#Filename:IfcPerformanceHistory.py
import log
import common
from ifccontrol import IFCCONTROL

from utils import *

class IFCPERFORMANCEHISTORY(IFCCONTROL):
    """"""
    def __init__(self,id,arg):
        super(IFCPERFORMANCEHISTORY,self).__init__(id,arg)
        self.type='IFCPERFORMANCEHISTORY'
        self.inverse={}
        self.LifeCyclePhase=None #IfcLabel


    def load(self):
        """register inverses"""
        if not super(IFCPERFORMANCEHISTORY,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCPERFORMANCEHISTORY,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.LifeCyclePhase= fromSPF(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCPERFORMANCEHISTORY,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCPERFORMANCEHISTORY,self).toString()       
        line += strToSPF(self.LifeCyclePhase)+','

        return line

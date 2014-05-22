#!/usr/bin/python
#coding=utf-8
#Filename:IfcWorkSchedule.py
import log
import common
from ifcworkcontrol import IFCWORKCONTROL

from utils import *

class IFCWORKSCHEDULE(IFCWORKCONTROL):
    """"""
    def __init__(self,id,arg):
        super(IFCWORKSCHEDULE,self).__init__(id,arg)
        self.type='IFCWORKSCHEDULE'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCWORKSCHEDULE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCWORKSCHEDULE,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCWORKSCHEDULE,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCWORKSCHEDULE,self).toString()       

        return line

#!/usr/bin/python
#coding=utf-8
#Filename:IfcRelSchedulesCostItems.py
import log
import common
from ifcrelassignstocontrol import IFCRELASSIGNSTOCONTROL

from utils import *

class IFCRELSCHEDULESCOSTITEMS(IFCRELASSIGNSTOCONTROL):
    """"""
    def __init__(self,id,arg):
        super(IFCRELSCHEDULESCOSTITEMS,self).__init__(id,arg)
        self.type='IFCRELSCHEDULESCOSTITEMS'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCRELSCHEDULESCOSTITEMS,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCRELSCHEDULESCOSTITEMS,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCRELSCHEDULESCOSTITEMS,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCRELSCHEDULESCOSTITEMS,self).toString()       

        return line

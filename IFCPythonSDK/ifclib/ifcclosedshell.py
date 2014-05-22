#!/usr/bin/python
#coding=utf-8
#Filename:IfcClosedShell.py
import log
import common
from ifcconnectedfaceset import IFCCONNECTEDFACESET

from utils import *

class IFCCLOSEDSHELL(IFCCONNECTEDFACESET):
    """"""
    def __init__(self,id,arg):
        super(IFCCLOSEDSHELL,self).__init__(id,arg)
        self.type='IFCCLOSEDSHELL'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCCLOSEDSHELL,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCLOSEDSHELL,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCLOSEDSHELL,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCCLOSEDSHELL,self).toString()       

        return line

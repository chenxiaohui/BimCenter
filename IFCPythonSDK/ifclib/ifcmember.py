#!/usr/bin/python
#coding=utf-8
#Filename:IfcMember.py
import log
import common
from ifcbuildingelement import IFCBUILDINGELEMENT

from utils import *

class IFCMEMBER(IFCBUILDINGELEMENT):
    """"""
    def __init__(self,id,arg):
        super(IFCMEMBER,self).__init__(id,arg)
        self.type='IFCMEMBER'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCMEMBER,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCMEMBER,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCMEMBER,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCMEMBER,self).toString()       

        return line

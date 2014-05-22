#!/usr/bin/python
#coding=utf-8
#Filename:IfcBuildingElementPart.py
import log
import common
from ifcbuildingelementcomponent import IFCBUILDINGELEMENTCOMPONENT

from utils import *

class IFCBUILDINGELEMENTPART(IFCBUILDINGELEMENTCOMPONENT):
    """"""
    def __init__(self,id,arg):
        super(IFCBUILDINGELEMENTPART,self).__init__(id,arg)
        self.type='IFCBUILDINGELEMENTPART'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCBUILDINGELEMENTPART,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCBUILDINGELEMENTPART,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCBUILDINGELEMENTPART,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCBUILDINGELEMENTPART,self).toString()       

        return line

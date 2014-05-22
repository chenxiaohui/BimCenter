#!/usr/bin/python
#coding=utf-8
#Filename:IfcBuildingElementComponent.py
import log
import common
from ifcbuildingelement import IFCBUILDINGELEMENT

from utils import *

class IFCBUILDINGELEMENTCOMPONENT(IFCBUILDINGELEMENT):
    """"""
    def __init__(self,id,arg):
        super(IFCBUILDINGELEMENTCOMPONENT,self).__init__(id,arg)
        self.type='IFCBUILDINGELEMENTCOMPONENT'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCBUILDINGELEMENTCOMPONENT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCBUILDINGELEMENTCOMPONENT,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCBUILDINGELEMENTCOMPONENT,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCBUILDINGELEMENTCOMPONENT,self).toString()       

        return line

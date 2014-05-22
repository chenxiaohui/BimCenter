#!/usr/bin/python
#coding=utf-8
#Filename:IfcCrewResource.py
import log
import common
from ifcconstructionresource import IFCCONSTRUCTIONRESOURCE

from utils import *

class IFCCREWRESOURCE(IFCCONSTRUCTIONRESOURCE):
    """"""
    def __init__(self,id,arg):
        super(IFCCREWRESOURCE,self).__init__(id,arg)
        self.type='IFCCREWRESOURCE'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCCREWRESOURCE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCREWRESOURCE,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCREWRESOURCE,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCCREWRESOURCE,self).toString()       

        return line

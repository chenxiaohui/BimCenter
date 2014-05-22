#!/usr/bin/python
#coding=utf-8
#Filename:IfcConstructionProductResource.py
import log
import common
from ifcconstructionresource import IFCCONSTRUCTIONRESOURCE

from utils import *

class IFCCONSTRUCTIONPRODUCTRESOURCE(IFCCONSTRUCTIONRESOURCE):
    """"""
    def __init__(self,id,arg):
        super(IFCCONSTRUCTIONPRODUCTRESOURCE,self).__init__(id,arg)
        self.type='IFCCONSTRUCTIONPRODUCTRESOURCE'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCCONSTRUCTIONPRODUCTRESOURCE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCONSTRUCTIONPRODUCTRESOURCE,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCONSTRUCTIONPRODUCTRESOURCE,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCCONSTRUCTIONPRODUCTRESOURCE,self).toString()       

        return line

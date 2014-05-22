#!/usr/bin/python
#coding=utf-8
#Filename:IfcLaborResource.py
import log
import common
from ifcconstructionresource import IFCCONSTRUCTIONRESOURCE

from utils import *

class IFCLABORRESOURCE(IFCCONSTRUCTIONRESOURCE):
    """"""
    def __init__(self,id,arg):
        super(IFCLABORRESOURCE,self).__init__(id,arg)
        self.type='IFCLABORRESOURCE'
        self.inverse={}
        self.SkillSet=None #IfcText


    def load(self):
        """register inverses"""
        if not super(IFCLABORRESOURCE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCLABORRESOURCE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.SkillSet= fromSPF(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCLABORRESOURCE,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCLABORRESOURCE,self).toString()       
        line += strToSPF(self.SkillSet)+','

        return line

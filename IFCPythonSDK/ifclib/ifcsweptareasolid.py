#!/usr/bin/python
#coding=utf-8
#Filename:IfcSweptAreaSolid.py
import log
import common
from ifcsolidmodel import IFCSOLIDMODEL

from utils import *

class IFCSWEPTAREASOLID(IFCSOLIDMODEL):
    """"""
    def __init__(self,id,arg):
        super(IFCSWEPTAREASOLID,self).__init__(id,arg)
        self.type='IFCSWEPTAREASOLID'
        self.inverse={}
        self.SweptArea=None #IfcProfileDef
        self.Position=None #IfcAxis2Placement3D


    def load(self):
        """register inverses"""
        if not super(IFCSWEPTAREASOLID,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSWEPTAREASOLID,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.SweptArea= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Position= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSWEPTAREASOLID,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCSWEPTAREASOLID,self).toString()       
        line += idToSPF(self.SweptArea)+','
        line += idToSPF(self.Position)+','

        return line

#!/usr/bin/python
#coding=utf-8
#Filename:IfcProject.py
import log
import common
from ifcobject import IFCOBJECT

from utils import *

class IFCPROJECT(IFCOBJECT):
    """"""
    def __init__(self,id,arg):
        super(IFCPROJECT,self).__init__(id,arg)
        self.type='IFCPROJECT'
        self.inverse={}
        self.LongName=None #IfcLabel
        self.Phase=None #IfcLabel
        self.RepresentationContexts=None #SET
        self.UnitsInContext=None #IfcUnitAssignment


    def load(self):
        """register inverses"""
        if not super(IFCPROJECT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCPROJECT,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.LongName= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Phase= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RepresentationContexts= getIdListParam(arg,spfToId)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.UnitsInContext= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCPROJECT,self).getAttrCount()+4

    def toString(self):
        """"""
        line=super(IFCPROJECT,self).toString()       
        line += strToSPF(self.LongName)+','
        line += strToSPF(self.Phase)+','
        line += listParamToSPF(self.RepresentationContexts,idToSPF)+','
        line += idToSPF(self.UnitsInContext)+','

        return line

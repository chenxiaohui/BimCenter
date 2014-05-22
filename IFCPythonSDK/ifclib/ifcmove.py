#!/usr/bin/python
#coding=utf-8
#Filename:IfcMove.py
import log
import common
from ifctask import IFCTASK

from utils import *

class IFCMOVE(IFCTASK):
    """"""
    def __init__(self,id,arg):
        super(IFCMOVE,self).__init__(id,arg)
        self.type='IFCMOVE'
        self.inverse={}
        self.MoveFrom=None #IfcSpatialStructureElement
        self.MoveTo=None #IfcSpatialStructureElement
        self.PunchList=None #LIST


    def load(self):
        """register inverses"""
        if not super(IFCMOVE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCMOVE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.MoveFrom= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.MoveTo= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PunchList= getIdListParam(arg,fromSPF)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCMOVE,self).getAttrCount()+3

    def toString(self):
        """"""
        line=super(IFCMOVE,self).toString()       
        line += idToSPF(self.MoveFrom)+','
        line += idToSPF(self.MoveTo)+','
        line += listParamToSPF(self.PunchList,strToSPF)+','

        return line

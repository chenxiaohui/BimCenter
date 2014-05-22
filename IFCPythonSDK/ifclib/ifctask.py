#!/usr/bin/python
#coding=utf-8
#Filename:IfcTask.py
import log
import common
from ifcprocess import IFCPROCESS

from utils import *

class IFCTASK(IFCPROCESS):
    """"""
    def __init__(self,id,arg):
        super(IFCTASK,self).__init__(id,arg)
        self.type='IFCTASK'
        self.inverse={}
        self.TaskId=None #IfcIdentifier
        self.Status=None #IfcLabel
        self.WorkMethod=None #IfcLabel
        self.IsMilestone=None #BOOLEAN
        self.Priority=None #INTEGER


    def load(self):
        """register inverses"""
        if not super(IFCTASK,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCTASK,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.TaskId= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Status= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.WorkMethod= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.IsMilestone= spfToLogical(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Priority= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCTASK,self).getAttrCount()+5

    def toString(self):
        """"""
        line=super(IFCTASK,self).toString()       
        line += strToSPF(self.TaskId)+','
        line += strToSPF(self.Status)+','
        line += strToSPF(self.WorkMethod)+','
        line += logicalToSPF(self.IsMilestone)+','
        line += integerToSPF(self.Priority)+','

        return line

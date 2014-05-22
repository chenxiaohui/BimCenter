#!/usr/bin/python
#coding=utf-8
#Filename:IfcProcedure.py
import log
import common
from ifcprocess import IFCPROCESS

from utils import *

class IFCPROCEDURE(IFCPROCESS):
    """"""
    def __init__(self,id,arg):
        super(IFCPROCEDURE,self).__init__(id,arg)
        self.type='IFCPROCEDURE'
        self.inverse={}
        self.ProcedureID=None #IfcIdentifier
        self.ProcedureType=None #IfcProcedureTypeEnum
        self.UserDefinedProcedureType=None #IfcLabel


    def load(self):
        """register inverses"""
        if not super(IFCPROCEDURE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCPROCEDURE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ProcedureID= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ProcedureType= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.UserDefinedProcedureType= fromSPF(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCPROCEDURE,self).getAttrCount()+3

    def toString(self):
        """"""
        line=super(IFCPROCEDURE,self).toString()       
        line += strToSPF(self.ProcedureID)+','
        line += typerefToSPF(self.ProcedureType)+','
        line += strToSPF(self.UserDefinedProcedureType)+','

        return line

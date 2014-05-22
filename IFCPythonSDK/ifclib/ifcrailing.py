#!/usr/bin/python
#coding=utf-8
#Filename:IfcRailing.py
import log
import common
from ifcbuildingelement import IFCBUILDINGELEMENT

from utils import *

class IFCRAILING(IFCBUILDINGELEMENT):
    """"""
    def __init__(self,id,arg):
        super(IFCRAILING,self).__init__(id,arg)
        self.type='IFCRAILING'
        self.inverse={}
        self.PredefinedType=None #IfcRailingTypeEnum


    def load(self):
        """register inverses"""
        if not super(IFCRAILING,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCRAILING,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PredefinedType= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCRAILING,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCRAILING,self).toString()       
        line += typerefToSPF(self.PredefinedType)+','

        return line

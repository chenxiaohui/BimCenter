#!/usr/bin/python
#coding=utf-8
#Filename:IfcRelAssociatesClassification.py
import log
import common
from ifcrelassociates import IFCRELASSOCIATES

from utils import *

class IFCRELASSOCIATESCLASSIFICATION(IFCRELASSOCIATES):
    """"""
    def __init__(self,id,arg):
        super(IFCRELASSOCIATESCLASSIFICATION,self).__init__(id,arg)
        self.type='IFCRELASSOCIATESCLASSIFICATION'
        self.inverse={}
        self.RelatingClassification=None #IfcClassificationNotationSelect


    def load(self):
        """register inverses"""
        if not super(IFCRELASSOCIATESCLASSIFICATION,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCRELASSOCIATESCLASSIFICATION,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatingClassification= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCRELASSOCIATESCLASSIFICATION,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCRELASSOCIATESCLASSIFICATION,self).toString()       
        line += typerefToSPF(self.RelatingClassification)+','

        return line

#!/usr/bin/python
#coding=utf-8
#Filename:IfcRelAssociatesDocument.py
import log
import common
from ifcrelassociates import IFCRELASSOCIATES

from utils import *

class IFCRELASSOCIATESDOCUMENT(IFCRELASSOCIATES):
    """"""
    def __init__(self,id,arg):
        super(IFCRELASSOCIATESDOCUMENT,self).__init__(id,arg)
        self.type='IFCRELASSOCIATESDOCUMENT'
        self.inverse={}
        self.RelatingDocument=None #IfcDocumentSelect


    def load(self):
        """register inverses"""
        if not super(IFCRELASSOCIATESDOCUMENT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCRELASSOCIATESDOCUMENT,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatingDocument= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCRELASSOCIATESDOCUMENT,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCRELASSOCIATESDOCUMENT,self).toString()       
        line += typerefToSPF(self.RelatingDocument)+','

        return line

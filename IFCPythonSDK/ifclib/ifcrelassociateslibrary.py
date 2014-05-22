#!/usr/bin/python
#coding=utf-8
#Filename:IfcRelAssociatesLibrary.py
import log
import common
from ifcrelassociates import IFCRELASSOCIATES

from utils import *

class IFCRELASSOCIATESLIBRARY(IFCRELASSOCIATES):
    """"""
    def __init__(self,id,arg):
        super(IFCRELASSOCIATESLIBRARY,self).__init__(id,arg)
        self.type='IFCRELASSOCIATESLIBRARY'
        self.inverse={}
        self.RelatingLibrary=None #IfcLibrarySelect


    def load(self):
        """register inverses"""
        if not super(IFCRELASSOCIATESLIBRARY,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCRELASSOCIATESLIBRARY,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatingLibrary= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCRELASSOCIATESLIBRARY,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCRELASSOCIATESLIBRARY,self).toString()       
        line += typerefToSPF(self.RelatingLibrary)+','

        return line

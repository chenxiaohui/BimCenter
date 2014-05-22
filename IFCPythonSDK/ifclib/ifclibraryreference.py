#!/usr/bin/python
#coding=utf-8
#Filename:IfcLibraryReference.py
import log
import common
from ifcexternalreference import IFCEXTERNALREFERENCE

from utils import *

class IFCLIBRARYREFERENCE(IFCEXTERNALREFERENCE):
    """"""
    def __init__(self,id,arg):
        super(IFCLIBRARYREFERENCE,self).__init__(id,arg)
        self.type='IFCLIBRARYREFERENCE'
        self.inverse={}
        self.inverse['ReferenceIntoLibrary']=[] #inverse:SET of IfcLibraryInformation


    def load(self):
        """register inverses"""
        if not super(IFCLIBRARYREFERENCE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCLIBRARYREFERENCE,self).init():
            return False

        inverses = self.args.getInverses('IFCLIBRARYINFORMATION', 'LibraryReference');
        if inverses:
            self.inverse['ReferenceIntoLibrary']=inverses

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCLIBRARYREFERENCE,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCLIBRARYREFERENCE,self).toString()       

        return line

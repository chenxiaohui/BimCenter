#!/usr/bin/python
#coding=utf-8
#Filename:IfcDocumentReference.py
import log
import common
from ifcexternalreference import IFCEXTERNALREFERENCE

from utils import *

class IFCDOCUMENTREFERENCE(IFCEXTERNALREFERENCE):
    """"""
    def __init__(self,id,arg):
        super(IFCDOCUMENTREFERENCE,self).__init__(id,arg)
        self.type='IFCDOCUMENTREFERENCE'
        self.inverse={}
        self.inverse['ReferenceToDocument']=[] #inverse:SET of IfcDocumentInformation


    def load(self):
        """register inverses"""
        if not super(IFCDOCUMENTREFERENCE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCDOCUMENTREFERENCE,self).init():
            return False

        inverses = self.args.getInverses('IFCDOCUMENTINFORMATION', 'DocumentReferences');
        if inverses:
            self.inverse['ReferenceToDocument']=inverses

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCDOCUMENTREFERENCE,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCDOCUMENTREFERENCE,self).toString()       

        return line

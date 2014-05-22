#!/usr/bin/python
#coding=utf-8
#Filename:IfcDocumentElectronicFormat.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCDOCUMENTELECTRONICFORMAT(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCDOCUMENTELECTRONICFORMAT,self).__init__(id,arg)
        self.type='IFCDOCUMENTELECTRONICFORMAT'
        self.inverse={}
        self.FileExtension=None #IfcLabel
        self.MimeContentType=None #IfcLabel
        self.MimeSubtype=None #IfcLabel


    def load(self):
        """register inverses"""
        if not super(IFCDOCUMENTELECTRONICFORMAT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCDOCUMENTELECTRONICFORMAT,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.FileExtension= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.MimeContentType= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.MimeSubtype= fromSPF(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCDOCUMENTELECTRONICFORMAT,self).getAttrCount()+3

    def toString(self):
        """"""
        line=super(IFCDOCUMENTELECTRONICFORMAT,self).toString()       
        line += strToSPF(self.FileExtension)+','
        line += strToSPF(self.MimeContentType)+','
        line += strToSPF(self.MimeSubtype)+','

        return line

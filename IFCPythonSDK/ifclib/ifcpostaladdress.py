#!/usr/bin/python
#coding=utf-8
#Filename:IfcPostalAddress.py
import log
import common
from ifcaddress import IFCADDRESS

from utils import *

class IFCPOSTALADDRESS(IFCADDRESS):
    """"""
    def __init__(self,id,arg):
        super(IFCPOSTALADDRESS,self).__init__(id,arg)
        self.type='IFCPOSTALADDRESS'
        self.inverse={}
        self.InternalLocation=None #IfcLabel
        self.AddressLines=None #LIST
        self.PostalBox=None #IfcLabel
        self.Town=None #IfcLabel
        self.Region=None #IfcLabel
        self.PostalCode=None #IfcLabel
        self.Country=None #IfcLabel


    def load(self):
        """register inverses"""
        if not super(IFCPOSTALADDRESS,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCPOSTALADDRESS,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.InternalLocation= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.AddressLines= getIdListParam(arg,fromSPF)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PostalBox= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Town= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Region= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PostalCode= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Country= fromSPF(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCPOSTALADDRESS,self).getAttrCount()+7

    def toString(self):
        """"""
        line=super(IFCPOSTALADDRESS,self).toString()       
        line += strToSPF(self.InternalLocation)+','
        line += listParamToSPF(self.AddressLines,strToSPF)+','
        line += strToSPF(self.PostalBox)+','
        line += strToSPF(self.Town)+','
        line += strToSPF(self.Region)+','
        line += strToSPF(self.PostalCode)+','
        line += strToSPF(self.Country)+','

        return line

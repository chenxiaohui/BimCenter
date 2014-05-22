#!/usr/bin/python
#coding=utf-8
#Filename:IfcTelecomAddress.py
import log
import common
from ifcaddress import IFCADDRESS

from utils import *

class IFCTELECOMADDRESS(IFCADDRESS):
    """"""
    def __init__(self,id,arg):
        super(IFCTELECOMADDRESS,self).__init__(id,arg)
        self.type='IFCTELECOMADDRESS'
        self.inverse={}
        self.TelephoneNumbers=None #LIST
        self.FacsimileNumbers=None #LIST
        self.PagerNumber=None #IfcLabel
        self.ElectronicMailAddresses=None #LIST
        self.WWWHomePageURL=None #IfcLabel


    def load(self):
        """register inverses"""
        if not super(IFCTELECOMADDRESS,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCTELECOMADDRESS,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.TelephoneNumbers= getIdListParam(arg,fromSPF)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.FacsimileNumbers= getIdListParam(arg,fromSPF)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.PagerNumber= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ElectronicMailAddresses= getIdListParam(arg,fromSPF)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.WWWHomePageURL= fromSPF(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCTELECOMADDRESS,self).getAttrCount()+5

    def toString(self):
        """"""
        line=super(IFCTELECOMADDRESS,self).toString()       
        line += listParamToSPF(self.TelephoneNumbers,strToSPF)+','
        line += listParamToSPF(self.FacsimileNumbers,strToSPF)+','
        line += strToSPF(self.PagerNumber)+','
        line += listParamToSPF(self.ElectronicMailAddresses,strToSPF)+','
        line += strToSPF(self.WWWHomePageURL)+','

        return line

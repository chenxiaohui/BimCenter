#!/usr/bin/python
#coding=utf-8
#Filename:IfcAddress.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCADDRESS(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCADDRESS,self).__init__(id,arg)
        self.type='IFCADDRESS'
        self.inverse={}
        self.Purpose=None #IfcAddressTypeEnum
        self.Description=None #IfcText
        self.UserDefinedPurpose=None #IfcLabel
        self.inverse['OfOrganization']=[] #inverse:SET of IfcOrganization
        self.inverse['OfPerson']=[] #inverse:SET of IfcPerson


    def load(self):
        """register inverses"""
        if not super(IFCADDRESS,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCADDRESS,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Purpose= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Description= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.UserDefinedPurpose= fromSPF(arg)

        inverses = self.args.getInverses('IFCORGANIZATION', 'Addresses');
        if inverses:
            self.inverse['OfOrganization']=inverses

        inverses = self.args.getInverses('IFCPERSON', 'Addresses');
        if inverses:
            self.inverse['OfPerson']=inverses

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCADDRESS,self).getAttrCount()+3

    def toString(self):
        """"""
        line=super(IFCADDRESS,self).toString()       
        line += typerefToSPF(self.Purpose)+','
        line += strToSPF(self.Description)+','
        line += strToSPF(self.UserDefinedPurpose)+','

        return line

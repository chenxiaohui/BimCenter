#!/usr/bin/python
#coding=utf-8
#Filename:IfcRelAssociatesProfileProperties.py
import log
import common
from ifcrelassociates import IFCRELASSOCIATES

from utils import *

class IFCRELASSOCIATESPROFILEPROPERTIES(IFCRELASSOCIATES):
    """"""
    def __init__(self,id,arg):
        super(IFCRELASSOCIATESPROFILEPROPERTIES,self).__init__(id,arg)
        self.type='IFCRELASSOCIATESPROFILEPROPERTIES'
        self.inverse={}
        self.RelatingProfileProperties=None #IfcProfileProperties
        self.ProfileSectionLocation=None #IfcShapeAspect
        self.ProfileOrientation=None #IfcOrientationSelect


    def load(self):
        """register inverses"""
        if not super(IFCRELASSOCIATESPROFILEPROPERTIES,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCRELASSOCIATESPROFILEPROPERTIES,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RelatingProfileProperties= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ProfileSectionLocation= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ProfileOrientation= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCRELASSOCIATESPROFILEPROPERTIES,self).getAttrCount()+3

    def toString(self):
        """"""
        line=super(IFCRELASSOCIATESPROFILEPROPERTIES,self).toString()       
        line += idToSPF(self.RelatingProfileProperties)+','
        line += idToSPF(self.ProfileSectionLocation)+','
        line += typerefToSPF(self.ProfileOrientation)+','

        return line

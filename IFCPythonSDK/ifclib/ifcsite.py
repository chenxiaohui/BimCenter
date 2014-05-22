#!/usr/bin/python
#coding=utf-8
#Filename:IfcSite.py
import log
import common
from ifcspatialstructureelement import IFCSPATIALSTRUCTUREELEMENT

from utils import *

class IFCSITE(IFCSPATIALSTRUCTUREELEMENT):
    """"""
    def __init__(self,id,arg):
        super(IFCSITE,self).__init__(id,arg)
        self.type='IFCSITE'
        self.inverse={}
        self.RefLatitude=None #IfcCompoundPlaneAngleMeasure
        self.RefLongitude=None #IfcCompoundPlaneAngleMeasure
        self.RefElevation=None #IfcLengthMeasure
        self.LandTitleNumber=None #IfcLabel
        self.SiteAddress=None #IfcPostalAddress


    def load(self):
        """register inverses"""
        if not super(IFCSITE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSITE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RefLatitude= getIdListParam(arg,spfToInteger)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RefLongitude= getIdListParam(arg,spfToInteger)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.RefElevation= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.LandTitleNumber= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.SiteAddress= spfToId(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSITE,self).getAttrCount()+5

    def toString(self):
        """"""
        line=super(IFCSITE,self).toString()       
        line += listParamToSPF(self.RefLatitude,integerToSPF)+','
        line += listParamToSPF(self.RefLongitude,integerToSPF)+','
        line += integerToSPF(self.RefElevation)+','
        line += strToSPF(self.LandTitleNumber)+','
        line += idToSPF(self.SiteAddress)+','

        return line

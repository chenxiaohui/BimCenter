#!/usr/bin/python
#coding=utf-8
#Filename:IfcQuantityVolume.py
import log
import common
from ifcphysicalsimplequantity import IFCPHYSICALSIMPLEQUANTITY

from utils import *

class IFCQUANTITYVOLUME(IFCPHYSICALSIMPLEQUANTITY):
    """"""
    def __init__(self,id,arg):
        super(IFCQUANTITYVOLUME,self).__init__(id,arg)
        self.type='IFCQUANTITYVOLUME'
        self.inverse={}
        self.VolumeValue=None #IfcVolumeMeasure


    def load(self):
        """register inverses"""
        if not super(IFCQUANTITYVOLUME,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCQUANTITYVOLUME,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.VolumeValue= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCQUANTITYVOLUME,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCQUANTITYVOLUME,self).toString()       
        line += integerToSPF(self.VolumeValue)+','

        return line

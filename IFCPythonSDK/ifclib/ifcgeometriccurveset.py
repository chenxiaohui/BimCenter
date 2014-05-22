#!/usr/bin/python
#coding=utf-8
#Filename:IfcGeometricCurveSet.py
import log
import common
from ifcgeometricset import IFCGEOMETRICSET

from utils import *

class IFCGEOMETRICCURVESET(IFCGEOMETRICSET):
    """"""
    def __init__(self,id,arg):
        super(IFCGEOMETRICCURVESET,self).__init__(id,arg)
        self.type='IFCGEOMETRICCURVESET'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCGEOMETRICCURVESET,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCGEOMETRICCURVESET,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCGEOMETRICCURVESET,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCGEOMETRICCURVESET,self).toString()       

        return line

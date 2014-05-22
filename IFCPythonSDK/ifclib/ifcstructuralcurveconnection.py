#!/usr/bin/python
#coding=utf-8
#Filename:IfcStructuralCurveConnection.py
import log
import common
from ifcstructuralconnection import IFCSTRUCTURALCONNECTION

from utils import *

class IFCSTRUCTURALCURVECONNECTION(IFCSTRUCTURALCONNECTION):
    """"""
    def __init__(self,id,arg):
        super(IFCSTRUCTURALCURVECONNECTION,self).__init__(id,arg)
        self.type='IFCSTRUCTURALCURVECONNECTION'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCSTRUCTURALCURVECONNECTION,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSTRUCTURALCURVECONNECTION,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSTRUCTURALCURVECONNECTION,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCSTRUCTURALCURVECONNECTION,self).toString()       

        return line

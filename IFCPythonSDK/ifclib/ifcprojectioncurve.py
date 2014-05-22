#!/usr/bin/python
#coding=utf-8
#Filename:IfcProjectionCurve.py
import log
import common
from ifcannotationcurveoccurrence import IFCANNOTATIONCURVEOCCURRENCE

from utils import *

class IFCPROJECTIONCURVE(IFCANNOTATIONCURVEOCCURRENCE):
    """"""
    def __init__(self,id,arg):
        super(IFCPROJECTIONCURVE,self).__init__(id,arg)
        self.type='IFCPROJECTIONCURVE'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCPROJECTIONCURVE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCPROJECTIONCURVE,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCPROJECTIONCURVE,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCPROJECTIONCURVE,self).toString()       

        return line

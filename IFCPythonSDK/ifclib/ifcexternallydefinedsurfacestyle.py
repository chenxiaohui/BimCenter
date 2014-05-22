#!/usr/bin/python
#coding=utf-8
#Filename:IfcExternallyDefinedSurfaceStyle.py
import log
import common
from ifcexternalreference import IFCEXTERNALREFERENCE

from utils import *

class IFCEXTERNALLYDEFINEDSURFACESTYLE(IFCEXTERNALREFERENCE):
    """"""
    def __init__(self,id,arg):
        super(IFCEXTERNALLYDEFINEDSURFACESTYLE,self).__init__(id,arg)
        self.type='IFCEXTERNALLYDEFINEDSURFACESTYLE'
        self.inverse={}


    def load(self):
        """register inverses"""
        if not super(IFCEXTERNALLYDEFINEDSURFACESTYLE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCEXTERNALLYDEFINEDSURFACESTYLE,self).init():
            return False

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCEXTERNALLYDEFINEDSURFACESTYLE,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCEXTERNALLYDEFINEDSURFACESTYLE,self).toString()       

        return line

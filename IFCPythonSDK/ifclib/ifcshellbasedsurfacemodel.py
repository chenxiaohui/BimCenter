#!/usr/bin/python
#coding=utf-8
#Filename:IfcShellBasedSurfaceModel.py
import log
import common
from ifcgeometricrepresentationitem import IFCGEOMETRICREPRESENTATIONITEM

from utils import *

class IFCSHELLBASEDSURFACEMODEL(IFCGEOMETRICREPRESENTATIONITEM):
    """"""
    def __init__(self,id,arg):
        super(IFCSHELLBASEDSURFACEMODEL,self).__init__(id,arg)
        self.type='IFCSHELLBASEDSURFACEMODEL'
        self.inverse={}
        self.SbsmBoundary=None #SET


    def load(self):
        """register inverses"""
        if not super(IFCSHELLBASEDSURFACEMODEL,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSHELLBASEDSURFACEMODEL,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.SbsmBoundary= getIdListParam(arg,spfToTypeRef)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSHELLBASEDSURFACEMODEL,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCSHELLBASEDSURFACEMODEL,self).toString()       
        line += listParamToSPF(self.SbsmBoundary,typerefToSPF)+','

        return line

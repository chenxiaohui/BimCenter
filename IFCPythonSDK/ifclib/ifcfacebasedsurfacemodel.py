#!/usr/bin/python
#coding=utf-8
#Filename:IfcFaceBasedSurfaceModel.py
import log
import common
from ifcgeometricrepresentationitem import IFCGEOMETRICREPRESENTATIONITEM

from utils import *

class IFCFACEBASEDSURFACEMODEL(IFCGEOMETRICREPRESENTATIONITEM):
    """"""
    def __init__(self,id,arg):
        super(IFCFACEBASEDSURFACEMODEL,self).__init__(id,arg)
        self.type='IFCFACEBASEDSURFACEMODEL'
        self.inverse={}
        self.FbsmFaces=None #SET


    def load(self):
        """register inverses"""
        if not super(IFCFACEBASEDSURFACEMODEL,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCFACEBASEDSURFACEMODEL,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.FbsmFaces= getIdListParam(arg,spfToId)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCFACEBASEDSURFACEMODEL,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCFACEBASEDSURFACEMODEL,self).toString()       
        line += listParamToSPF(self.FbsmFaces,idToSPF)+','

        return line

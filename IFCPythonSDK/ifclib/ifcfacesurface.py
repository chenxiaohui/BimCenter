#!/usr/bin/python
#coding=utf-8
#Filename:IfcFaceSurface.py
import log
import common
from ifcface import IFCFACE

from utils import *

class IFCFACESURFACE(IFCFACE):
    """"""
    def __init__(self,id,arg):
        super(IFCFACESURFACE,self).__init__(id,arg)
        self.type='IFCFACESURFACE'
        self.inverse={}
        self.FaceSurface=None #IfcSurface
        self.SameSense=None #BOOLEAN


    def load(self):
        """register inverses"""
        if not super(IFCFACESURFACE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCFACESURFACE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.FaceSurface= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.SameSense= spfToLogical(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCFACESURFACE,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCFACESURFACE,self).toString()       
        line += idToSPF(self.FaceSurface)+','
        line += logicalToSPF(self.SameSense)+','

        return line

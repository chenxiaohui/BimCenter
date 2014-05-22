#!/usr/bin/python
#coding=utf-8
#Filename:IfcStructuralLoadSingleDisplacementDistortion.py
import log
import common
from ifcstructuralloadsingledisplacement import IFCSTRUCTURALLOADSINGLEDISPLACEMENT

from utils import *

class IFCSTRUCTURALLOADSINGLEDISPLACEMENTDISTORTION(IFCSTRUCTURALLOADSINGLEDISPLACEMENT):
    """"""
    def __init__(self,id,arg):
        super(IFCSTRUCTURALLOADSINGLEDISPLACEMENTDISTORTION,self).__init__(id,arg)
        self.type='IFCSTRUCTURALLOADSINGLEDISPLACEMENTDISTORTION'
        self.inverse={}
        self.Distortion=None #IfcCurvatureMeasure


    def load(self):
        """register inverses"""
        if not super(IFCSTRUCTURALLOADSINGLEDISPLACEMENTDISTORTION,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSTRUCTURALLOADSINGLEDISPLACEMENTDISTORTION,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Distortion= spfToInteger(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSTRUCTURALLOADSINGLEDISPLACEMENTDISTORTION,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCSTRUCTURALLOADSINGLEDISPLACEMENTDISTORTION,self).toString()       
        line += integerToSPF(self.Distortion)+','

        return line

#!/usr/bin/python
#coding=utf-8
#Filename:IfcSoundProperties.py
import log
import common
from ifcpropertysetdefinition import IFCPROPERTYSETDEFINITION

from utils import *

class IFCSOUNDPROPERTIES(IFCPROPERTYSETDEFINITION):
    """"""
    def __init__(self,id,arg):
        super(IFCSOUNDPROPERTIES,self).__init__(id,arg)
        self.type='IFCSOUNDPROPERTIES'
        self.inverse={}
        self.IsAttenuating=None #IfcBoolean
        self.SoundScale=None #IfcSoundScaleEnum
        self.SoundValues=None #LIST


    def load(self):
        """register inverses"""
        if not super(IFCSOUNDPROPERTIES,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCSOUNDPROPERTIES,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.IsAttenuating= spfToLogical(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.SoundScale= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.SoundValues= getIdListParam(arg,spfToId)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCSOUNDPROPERTIES,self).getAttrCount()+3

    def toString(self):
        """"""
        line=super(IFCSOUNDPROPERTIES,self).toString()       
        line += logicalToSPF(self.IsAttenuating)+','
        line += typerefToSPF(self.SoundScale)+','
        line += listParamToSPF(self.SoundValues,idToSPF)+','

        return line

#!/usr/bin/python
#coding=utf-8
#Filename:IfcTextStyleWithBoxCharacteristics.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCTEXTSTYLEWITHBOXCHARACTERISTICS(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCTEXTSTYLEWITHBOXCHARACTERISTICS,self).__init__(id,arg)
        self.type='IFCTEXTSTYLEWITHBOXCHARACTERISTICS'
        self.inverse={}
        self.BoxHeight=None #IfcPositiveLengthMeasure
        self.BoxWidth=None #IfcPositiveLengthMeasure
        self.BoxSlantAngle=None #IfcPlaneAngleMeasure
        self.BoxRotateAngle=None #IfcPlaneAngleMeasure
        self.CharacterSpacing=None #IfcSizeSelect


    def load(self):
        """register inverses"""
        if not super(IFCTEXTSTYLEWITHBOXCHARACTERISTICS,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCTEXTSTYLEWITHBOXCHARACTERISTICS,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.BoxHeight= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.BoxWidth= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.BoxSlantAngle= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.BoxRotateAngle= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.CharacterSpacing= spfToTypeRef(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCTEXTSTYLEWITHBOXCHARACTERISTICS,self).getAttrCount()+5

    def toString(self):
        """"""
        line=super(IFCTEXTSTYLEWITHBOXCHARACTERISTICS,self).toString()       
        line += integerToSPF(self.BoxHeight)+','
        line += integerToSPF(self.BoxWidth)+','
        line += integerToSPF(self.BoxSlantAngle)+','
        line += integerToSPF(self.BoxRotateAngle)+','
        line += typerefToSPF(self.CharacterSpacing)+','

        return line

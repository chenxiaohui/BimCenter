#!/usr/bin/python
#coding=utf-8
#Filename:IfcRectangularTrimmedSurface.py
import log
import common
from ifcboundedsurface import IFCBOUNDEDSURFACE

from utils import *

class IFCRECTANGULARTRIMMEDSURFACE(IFCBOUNDEDSURFACE):
    """"""
    def __init__(self,id,arg):
        super(IFCRECTANGULARTRIMMEDSURFACE,self).__init__(id,arg)
        self.type='IFCRECTANGULARTRIMMEDSURFACE'
        self.inverse={}
        self.BasisSurface=None #IfcSurface
        self.U1=None #IfcParameterValue
        self.V1=None #IfcParameterValue
        self.U2=None #IfcParameterValue
        self.V2=None #IfcParameterValue
        self.Usense=None #BOOLEAN
        self.Vsense=None #BOOLEAN


    def load(self):
        """register inverses"""
        if not super(IFCRECTANGULARTRIMMEDSURFACE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCRECTANGULARTRIMMEDSURFACE,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.BasisSurface= spfToId(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.U1= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.V1= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.U2= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.V2= spfToInteger(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Usense= spfToLogical(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Vsense= spfToLogical(arg)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCRECTANGULARTRIMMEDSURFACE,self).getAttrCount()+7

    def toString(self):
        """"""
        line=super(IFCRECTANGULARTRIMMEDSURFACE,self).toString()       
        line += idToSPF(self.BasisSurface)+','
        line += integerToSPF(self.U1)+','
        line += integerToSPF(self.V1)+','
        line += integerToSPF(self.U2)+','
        line += integerToSPF(self.V2)+','
        line += logicalToSPF(self.Usense)+','
        line += logicalToSPF(self.Vsense)+','

        return line

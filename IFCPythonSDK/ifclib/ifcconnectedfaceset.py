#!/usr/bin/python
#coding=utf-8
#Filename:IfcConnectedFaceSet.py
import log
import common
from ifctopologicalrepresentationitem import IFCTOPOLOGICALREPRESENTATIONITEM

from utils import *

class IFCCONNECTEDFACESET(IFCTOPOLOGICALREPRESENTATIONITEM):
    """"""
    def __init__(self,id,arg):
        super(IFCCONNECTEDFACESET,self).__init__(id,arg)
        self.type='IFCCONNECTEDFACESET'
        self.inverse={}
        self.CfsFaces=None #SET


    def load(self):
        """register inverses"""
        if not super(IFCCONNECTEDFACESET,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCONNECTEDFACESET,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.CfsFaces= getIdListParam(arg,spfToId)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCONNECTEDFACESET,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCCONNECTEDFACESET,self).toString()       
        line += listParamToSPF(self.CfsFaces,idToSPF)+','

        return line

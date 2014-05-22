#!/usr/bin/python
#coding=utf-8
#Filename:IfcReinforcementDefinitionProperties.py
import log
import common
from ifcpropertysetdefinition import IFCPROPERTYSETDEFINITION

from utils import *

class IFCREINFORCEMENTDEFINITIONPROPERTIES(IFCPROPERTYSETDEFINITION):
    """"""
    def __init__(self,id,arg):
        super(IFCREINFORCEMENTDEFINITIONPROPERTIES,self).__init__(id,arg)
        self.type='IFCREINFORCEMENTDEFINITIONPROPERTIES'
        self.inverse={}
        self.DefinitionType=None #IfcLabel
        self.ReinforcementSectionDefinitions=None #LIST


    def load(self):
        """register inverses"""
        if not super(IFCREINFORCEMENTDEFINITIONPROPERTIES,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCREINFORCEMENTDEFINITIONPROPERTIES,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.DefinitionType= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ReinforcementSectionDefinitions= getIdListParam(arg,spfToId)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCREINFORCEMENTDEFINITIONPROPERTIES,self).getAttrCount()+2

    def toString(self):
        """"""
        line=super(IFCREINFORCEMENTDEFINITIONPROPERTIES,self).toString()       
        line += strToSPF(self.DefinitionType)+','
        line += listParamToSPF(self.ReinforcementSectionDefinitions,idToSPF)+','

        return line

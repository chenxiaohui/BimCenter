#!/usr/bin/python
#coding=utf-8
#Filename:IfcFacetedBrepWithVoids.py
import log
import common
from ifcmanifoldsolidbrep import IFCMANIFOLDSOLIDBREP

from utils import *

class IFCFACETEDBREPWITHVOIDS(IFCMANIFOLDSOLIDBREP):
    """"""
    def __init__(self,id,arg):
        super(IFCFACETEDBREPWITHVOIDS,self).__init__(id,arg)
        self.type='IFCFACETEDBREPWITHVOIDS'
        self.inverse={}
        self.Voids=None #SET


    def load(self):
        """register inverses"""
        if not super(IFCFACETEDBREPWITHVOIDS,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCFACETEDBREPWITHVOIDS,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Voids= getIdListParam(arg,spfToId)

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCFACETEDBREPWITHVOIDS,self).getAttrCount()+1

    def toString(self):
        """"""
        line=super(IFCFACETEDBREPWITHVOIDS,self).toString()       
        line += listParamToSPF(self.Voids,idToSPF)+','

        return line

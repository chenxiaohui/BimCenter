#!/usr/bin/python
#coding=utf-8
#Filename:IfcProcess.py
import log
import common
from ifcobject import IFCOBJECT

from utils import *

class IFCPROCESS(IFCOBJECT):
    """"""
    def __init__(self,id,arg):
        super(IFCPROCESS,self).__init__(id,arg)
        self.type='IFCPROCESS'
        self.inverse={}
        self.inverse['OperatesOn']=[] #inverse:SET of IfcRelAssignsToProcess
        self.inverse['IsSuccessorFrom']=[] #inverse:SET of IfcRelSequence
        self.inverse['IsPredecessorTo']=[] #inverse:SET of IfcRelSequence


    def load(self):
        """register inverses"""
        if not super(IFCPROCESS,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCPROCESS,self).init():
            return False

        inverses = self.args.getInverses('IFCRELASSIGNSTOPROCESS', 'RelatingProcess');
        if inverses:
            self.inverse['OperatesOn']=inverses

        inverses = self.args.getInverses('IFCRELSEQUENCE', 'RelatedProcess');
        if inverses:
            self.inverse['IsSuccessorFrom']=inverses

        inverses = self.args.getInverses('IFCRELSEQUENCE', 'RelatingProcess');
        if inverses:
            self.inverse['IsPredecessorTo']=inverses

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCPROCESS,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCPROCESS,self).toString()       

        return line

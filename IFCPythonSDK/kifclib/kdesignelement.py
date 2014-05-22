#!/usr/bin/python
#coding=utf-8
#Filename:KDesignElement.py
import log
import common
from kdimension import KDIMENSION

from utils import *

class KDESIGNELEMENT(KDIMENSION):
    """"""
    def __init__(self,id,arg):
        super(KDESIGNELEMENT,self).__init__(id,arg)
        self.type='KDESIGNELEMENT'
        self.inverse={}
        self.Name='' #KTEXT
        self.inverse['Belongs']=[] #inverse:SET of KRelBelongedToElement


    def load(self):
        """register inverses"""
        if not super(KDESIGNELEMENT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(KDESIGNELEMENT,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Name= fromSPF(arg)

        inverses = self.args.getInverses('KRELBELONGEDTOELEMENT', 'Owner');
        if inverses:
            self.inverse['Belongs']=inverses

        return True

    def getAttrCount(self):
        """"""
        return super(KDESIGNELEMENT,self).getAttrCount()+1

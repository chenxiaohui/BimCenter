#!/usr/bin/python
#coding=utf-8
#Filename:KDocument.py
import log
import common
from kroot import KROOT

from utils import *

class KDOCUMENT(KROOT):
    """"""
    def __init__(self,id,arg):
        super(KDOCUMENT,self).__init__(id,arg)
        self.type='KDOCUMENT'
        self.inverse={}
        self.Name='' #KTEXT
        self.Type='' #KTEXT
        self.URL='' #KTEXT
        self.inverse['IsBelongedToProject']=[] #inverse:SET of KRelBelongedToProject
        self.inverse['IsBelongedToElement']=[] #inverse:SET of KRelBelongedToElement


    def load(self):
        """register inverses"""
        if not super(KDOCUMENT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(KDOCUMENT,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Name= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Type= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.URL= fromSPF(arg)

        inverses = self.args.getInverses('KRELBELONGEDTOPROJECT', 'Documents');
        if inverses:
            self.inverse['IsBelongedToProject']=inverses

        inverses = self.args.getInverses('KRELBELONGEDTOELEMENT', 'Documents');
        if inverses:
            self.inverse['IsBelongedToElement']=inverses

        return True

    def getAttrCount(self):
        """"""
        return super(KDOCUMENT,self).getAttrCount()+3

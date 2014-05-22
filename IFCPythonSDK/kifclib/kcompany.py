#!/usr/bin/python
#coding=utf-8
#Filename:KCompany.py
import log
import common
from kroot import KROOT

from utils import *

class KCOMPANY(KROOT):
    """"""
    def __init__(self,id,arg):
        super(KCOMPANY,self).__init__(id,arg)
        self.type='KCOMPANY'
        self.inverse={}
        self.Name='' #KTEXT
        self.Place='' #KTEXT
        self.inverse['Completes']=[] #inverse:SET of KRelParticipate


    def load(self):
        """register inverses"""
        if not super(KCOMPANY,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(KCOMPANY,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Name= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Place= fromSPF(arg)

        inverses = self.args.getInverses('KRELPARTICIPATE', 'Participant');
        if inverses:
            self.inverse['Completes']=inverses

        return True

    def getAttrCount(self):
        """"""
        return super(KCOMPANY,self).getAttrCount()+2

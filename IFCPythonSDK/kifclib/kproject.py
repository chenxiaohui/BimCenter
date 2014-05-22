#!/usr/bin/python
#coding=utf-8
#Filename:KProject.py
import log
import common
from kdimension import KDIMENSION

from utils import *

class KPROJECT(KDIMENSION):
    """"""
    def __init__(self,id,arg):
        super(KPROJECT,self).__init__(id,arg)
        self.type='KPROJECT'
        self.inverse={}
        self.Name='' #KTEXT
        self.inverse['Belongs']=[] #inverse:SET of KRelBelongedToProject
        self.inverse['IsCompletedBy']=[] #inverse:SET of KRelParticipate


    def load(self):
        """register inverses"""
        if not super(KPROJECT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(KPROJECT,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Name= fromSPF(arg)

        inverses = self.args.getInverses('KRELBELONGEDTOPROJECT', 'Owner');
        if inverses:
            self.inverse['Belongs']=inverses

        inverses = self.args.getInverses('KRELPARTICIPATE', 'Project');
        if inverses:
            self.inverse['IsCompletedBy']=inverses

        return True

    def getAttrCount(self):
        """"""
        return super(KPROJECT,self).getAttrCount()+1

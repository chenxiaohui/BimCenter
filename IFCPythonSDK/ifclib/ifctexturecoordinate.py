#!/usr/bin/python
#coding=utf-8
#Filename:IfcTextureCoordinate.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCTEXTURECOORDINATE(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCTEXTURECOORDINATE,self).__init__(id,arg)
        self.type='IFCTEXTURECOORDINATE'
        self.inverse={}
        self.inverse['AnnotatedSurface']=[] #inverse:SET of IfcAnnotationSurface


    def load(self):
        """register inverses"""
        if not super(IFCTEXTURECOORDINATE,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCTEXTURECOORDINATE,self).init():
            return False

        inverses = self.args.getInverses('IFCANNOTATIONSURFACE', 'TextureCoordinates');
        if inverses:
            self.inverse['AnnotatedSurface']=inverses

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCTEXTURECOORDINATE,self).getAttrCount()+0

    def toString(self):
        """"""
        line=super(IFCTEXTURECOORDINATE,self).toString()       

        return line

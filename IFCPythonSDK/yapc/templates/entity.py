#!/usr/bin/python
#coding=utf-8
#Filename:{name}.py
import log
import common
{superimport}
from utils import *

class {name|upper}({superclass}):
    """"""
    def __init__(self,id,arg):
        super({name|upper},self).__init__(id,arg)
        self.type='{name|upper}'
        self.inverse={}
{definations}

    def load(self):
        """register inverses"""
        if not super({name|upper},self).load():
            return False
{load}
        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super({name|upper},self).init():
            return False
{init}
        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super({name|upper},self).getAttrCount()+{attrcount}

    def toString(self):
        """"""
        line=super({name|upper},self).toString()       
{tostring}
        return line

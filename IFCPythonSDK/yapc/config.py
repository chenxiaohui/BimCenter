#!/usr/bin/python
#coding=utf-8
#Filename:config.py

import ConfigParser
import os
cf=ConfigParser.ConfigParser()
HERE = os.path.dirname(os.path.abspath(__file__))
configFilePath=os.path.join(HERE,"yapc.conf").replace('\\','/')
cf.read(configFilePath)

def get(section,name):
    """"""
    return cf.get(section,name)


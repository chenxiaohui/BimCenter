#!/usr/bin/python
#coding=utf-8
#Filename:IfcShell.py

#TYPE IfcShell = SELECT
	#(IfcClosedShell,IfcOpenShell);
#END_TYPE;

class IfcShell(object):
    """"""
    def __init__(self,obj):
        super(IfcShell,self).__init__()
        self.lid=obj.lid
        self.m_type=obj.type
        

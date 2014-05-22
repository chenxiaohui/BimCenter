#!/usr/bin/python
#coding=utf-8
#Filename:IfcVectorOrDirection.py

#TYPE IfcVectorOrDirection = SELECT
	#(IfcDirection,IfcVector);
#END_TYPE;

class IfcVectorOrDirection(object):
    """"""
    def __init__(self,obj):
        super(IfcVectorOrDirection,self).__init__()
        self.lid=obj.lid
        self.m_type=obj.type
        

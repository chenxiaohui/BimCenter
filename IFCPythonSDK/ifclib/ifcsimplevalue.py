#!/usr/bin/python
#coding=utf-8
#Filename:IfcSimpleValue.py

#TYPE IfcSimpleValue = SELECT
	#(IfcInteger,IfcReal,IfcBoolean,IfcIdentifier,IfcText,IfcLabel,IfcLogical);
#END_TYPE;

class IfcSimpleValue(object):
    """"""
    def __init__(self,obj):
        super(IfcSimpleValue,self).__init__()
        self.lid=obj.lid
        self.m_type=obj.type
        

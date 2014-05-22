#!/usr/bin/python
#coding=utf-8
#Filename:IfcValue.py

#TYPE IfcValue = SELECT
	#(IfcMeasureValue,IfcSimpleValue,IfcDerivedMeasureValue);
#END_TYPE;

class IfcValue(object):
    """"""
    def __init__(self,obj):
        super(IfcValue,self).__init__()
        self.lid=obj.lid
        self.m_type=obj.type
        

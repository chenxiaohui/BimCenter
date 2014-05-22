#!/usr/bin/python
#coding=utf-8
#Filename:IfcTrimmingSelect.py

#TYPE IfcTrimmingSelect = SELECT
	#(IfcCartesianPoint,IfcParameterValue);
#END_TYPE;

class IfcTrimmingSelect(object):
    """"""
    def __init__(self,obj):
        super(IfcTrimmingSelect,self).__init__()
        self.lid=obj.lid
        self.m_type=obj.type
        

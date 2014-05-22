#!/usr/bin/python
#coding=utf-8
#Filename:IfcCsgSelect.py

#TYPE IfcCsgSelect = SELECT
	#(IfcBooleanResult,IfcCsgPrimitive3D);
#END_TYPE;

class IfcCsgSelect(object):
    """"""
    def __init__(self,obj):
        super(IfcCsgSelect,self).__init__()
        self.lid=obj.lid
        self.m_type=obj.type
        

#!/usr/bin/python
#coding=utf-8
#Filename:IfcGeometricSetSelect.py

#TYPE IfcGeometricSetSelect = SELECT
	#(IfcPoint,IfcCurve,IfcSurface);
#END_TYPE;

class IfcGeometricSetSelect(object):
    """"""
    def __init__(self,obj):
        super(IfcGeometricSetSelect,self).__init__()
        self.lid=obj.lid
        self.m_type=obj.type
        

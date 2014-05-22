#!/usr/bin/python
#coding=utf-8
#Filename:IfcOrientationSelect.py

#TYPE IfcOrientationSelect = SELECT
	#(IfcPlaneAngleMeasure,IfcDirection);
#END_TYPE;

class IfcOrientationSelect(object):
    """"""
    def __init__(self,obj):
        super(IfcOrientationSelect,self).__init__()
        self.lid=obj.lid
        self.m_type=obj.type
        

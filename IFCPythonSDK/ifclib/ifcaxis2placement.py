#!/usr/bin/python
#coding=utf-8
#Filename:IfcAxis2Placement.py

#TYPE IfcAxis2Placement = SELECT
	#(IfcAxis2Placement2D,IfcAxis2Placement3D);
#END_TYPE;

class IfcAxis2Placement(object):
    """"""
    def __init__(self,obj):
        super(IfcAxis2Placement,self).__init__()
        self.lid=obj.lid
        self.m_type=obj.type
        

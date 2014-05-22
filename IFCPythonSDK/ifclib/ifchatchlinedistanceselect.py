#!/usr/bin/python
#coding=utf-8
#Filename:IfcHatchLineDistanceSelect.py

#TYPE IfcHatchLineDistanceSelect = SELECT
	#(IfcOneDirectionRepeatFactor,IfcPositiveLengthMeasure);
#END_TYPE;

class IfcHatchLineDistanceSelect(object):
    """"""
    def __init__(self,obj):
        super(IfcHatchLineDistanceSelect,self).__init__()
        self.lid=obj.lid
        self.m_type=obj.type
        

#!/usr/bin/python
#coding=utf-8
#Filename:IfcSizeSelect.py

#TYPE IfcSizeSelect = SELECT
	#(IfcRatioMeasure,IfcLengthMeasure,IfcDescriptiveMeasure,IfcPositiveLengthMeasure,IfcNormalisedRatioMeasure,IfcPositiveRatioMeasure);
#END_TYPE;

class IfcSizeSelect(object):
    """"""
    def __init__(self,obj):
        super(IfcSizeSelect,self).__init__()
        self.lid=obj.lid
        self.m_type=obj.type
        

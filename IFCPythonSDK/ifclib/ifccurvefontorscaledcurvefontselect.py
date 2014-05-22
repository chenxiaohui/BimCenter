#!/usr/bin/python
#coding=utf-8
#Filename:IfcCurveFontOrScaledCurveFontSelect.py

#TYPE IfcCurveFontOrScaledCurveFontSelect = SELECT
	#(IfcCurveStyleFontSelect,IfcCurveStyleFontAndScaling);
#END_TYPE;

class IfcCurveFontOrScaledCurveFontSelect(object):
    """"""
    def __init__(self,obj):
        super(IfcCurveFontOrScaledCurveFontSelect,self).__init__()
        self.lid=obj.lid
        self.m_type=obj.type
        

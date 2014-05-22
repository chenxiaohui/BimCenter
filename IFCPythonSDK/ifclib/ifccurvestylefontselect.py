#!/usr/bin/python
#coding=utf-8
#Filename:IfcCurveStyleFontSelect.py

#TYPE IfcCurveStyleFontSelect = SELECT
	#(IfcPreDefinedCurveFont,IfcCurveStyleFont);
#END_TYPE;

class IfcCurveStyleFontSelect(object):
    """"""
    def __init__(self,obj):
        super(IfcCurveStyleFontSelect,self).__init__()
        self.lid=obj.lid
        self.m_type=obj.type
        

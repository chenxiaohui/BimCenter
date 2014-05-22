#!/usr/bin/python
#coding=utf-8
#Filename:IfcPresentationStyleSelect.py

#TYPE IfcPresentationStyleSelect = SELECT
	#(IfcNullStyle,IfcCurveStyle,IfcSymbolStyle,IfcFillAreaStyle,IfcTextStyle,IfcSurfaceStyle);
#END_TYPE;

class IfcPresentationStyleSelect(object):
    """"""
    def __init__(self,obj):
        super(IfcPresentationStyleSelect,self).__init__()
        self.lid=obj.lid
        self.m_type=obj.type
        

#!/usr/bin/python
#coding=utf-8
#Filename:IfcColourOrFactor.py

#TYPE IfcColourOrFactor = SELECT
	#(IfcColourRgb,IfcNormalisedRatioMeasure);
#END_TYPE;

class IfcColourOrFactor(object):
    """"""
    def __init__(self,obj):
        super(IfcColourOrFactor,self).__init__()
        self.lid=obj.lid
        self.m_type=obj.type
        

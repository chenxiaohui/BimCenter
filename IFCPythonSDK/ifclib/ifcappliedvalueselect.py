#!/usr/bin/python
#coding=utf-8
#Filename:IfcAppliedValueSelect.py

#TYPE IfcAppliedValueSelect = SELECT
	#(IfcRatioMeasure,IfcMeasureWithUnit,IfcMonetaryMeasure);
#END_TYPE;

class IfcAppliedValueSelect(object):
    """"""
    def __init__(self,obj):
        super(IfcAppliedValueSelect,self).__init__()
        self.lid=obj.lid
        self.m_type=obj.type
        

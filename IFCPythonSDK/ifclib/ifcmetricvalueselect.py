#!/usr/bin/python
#coding=utf-8
#Filename:IfcMetricValueSelect.py

#TYPE IfcMetricValueSelect = SELECT
	#(IfcDateTimeSelect,IfcMeasureWithUnit,IfcTable,IfcText,IfcTimeSeries,IfcCostValue);
#END_TYPE;

class IfcMetricValueSelect(object):
    """"""
    def __init__(self,obj):
        super(IfcMetricValueSelect,self).__init__()
        self.lid=obj.lid
        self.m_type=obj.type
        

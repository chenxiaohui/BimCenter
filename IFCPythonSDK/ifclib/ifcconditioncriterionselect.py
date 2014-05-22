#!/usr/bin/python
#coding=utf-8
#Filename:IfcConditionCriterionSelect.py

#TYPE IfcConditionCriterionSelect = SELECT
	#(IfcLabel,IfcMeasureWithUnit);
#END_TYPE;

class IfcConditionCriterionSelect(object):
    """"""
    def __init__(self,obj):
        super(IfcConditionCriterionSelect,self).__init__()
        self.lid=obj.lid
        self.m_type=obj.type
        

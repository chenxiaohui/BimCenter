#!/usr/bin/python
#coding=utf-8
#Filename:IfcDateTimeSelect.py

#TYPE IfcDateTimeSelect = SELECT
	#(IfcCalendarDate,IfcLocalTime,IfcDateAndTime);
#END_TYPE;

class IfcDateTimeSelect(object):
    """"""
    def __init__(self,obj):
        super(IfcDateTimeSelect,self).__init__()
        self.lid=obj.lid
        self.m_type=obj.type
        

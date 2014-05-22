#!/usr/bin/python
#coding=utf-8
#Filename:IfcObjectReferenceSelect.py

#TYPE IfcObjectReferenceSelect = SELECT
	#(IfcMaterial,IfcPerson,IfcDateAndTime,IfcMaterialList,IfcOrganization,IfcCalendarDate,IfcLocalTime,IfcPersonAndOrganization,IfcMaterialLayer,IfcExternalReference,IfcTimeSeries,IfcAddress,IfcAppliedValue);
#END_TYPE;

class IfcObjectReferenceSelect(object):
    """"""
    def __init__(self,obj):
        super(IfcObjectReferenceSelect,self).__init__()
        self.lid=obj.lid
        self.m_type=obj.type
        

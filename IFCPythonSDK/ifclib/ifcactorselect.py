#!/usr/bin/python
#coding=utf-8
#Filename:IfcActorSelect.py

#TYPE IfcActorSelect = SELECT
	#(IfcOrganization,IfcPerson,IfcPersonAndOrganization);
#END_TYPE;

class IfcActorSelect(object):
    """"""
    def __init__(self,obj):
        super(IfcActorSelect,self).__init__()
        self.lid=obj.lid
        self.m_type=obj.type
        

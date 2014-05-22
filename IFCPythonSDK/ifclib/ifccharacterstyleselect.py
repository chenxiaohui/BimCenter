#!/usr/bin/python
#coding=utf-8
#Filename:IfcCharacterStyleSelect.py

#TYPE IfcCharacterStyleSelect = SELECT
	#(IfcTextStyleForDefinedFont);
#END_TYPE;

class IfcCharacterStyleSelect(object):
    """"""
    def __init__(self,obj):
        super(IfcCharacterStyleSelect,self).__init__()
        self.lid=obj.lid
        self.m_type=obj.type
        

#!/usr/bin/python
#coding=utf-8
#Filename:IfcSymbolStyleSelect.py

#TYPE IfcSymbolStyleSelect = SELECT
	#(IfcColour);
#END_TYPE;

class IfcSymbolStyleSelect(object):
    """"""
    def __init__(self,obj):
        super(IfcSymbolStyleSelect,self).__init__()
        self.lid=obj.lid
        self.m_type=obj.type
        

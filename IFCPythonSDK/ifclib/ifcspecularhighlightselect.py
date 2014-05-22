#!/usr/bin/python
#coding=utf-8
#Filename:IfcSpecularHighlightSelect.py

#TYPE IfcSpecularHighlightSelect = SELECT
	#(IfcSpecularExponent,IfcSpecularRoughness);
#END_TYPE;

class IfcSpecularHighlightSelect(object):
    """"""
    def __init__(self,obj):
        super(IfcSpecularHighlightSelect,self).__init__()
        self.lid=obj.lid
        self.m_type=obj.type
        

#!/usr/bin/python
#coding=utf-8
#Filename:IfcFillStyleSelect.py

#TYPE IfcFillStyleSelect = SELECT
	#(IfcFillAreaStyleHatching,IfcFillAreaStyleTiles,IfcColour,IfcExternallyDefinedHatchStyle);
#END_TYPE;

class IfcFillStyleSelect(object):
    """"""
    def __init__(self,obj):
        super(IfcFillStyleSelect,self).__init__()
        self.lid=obj.lid
        self.m_type=obj.type
        

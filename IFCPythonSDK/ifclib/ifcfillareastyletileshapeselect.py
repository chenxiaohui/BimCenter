#!/usr/bin/python
#coding=utf-8
#Filename:IfcFillAreaStyleTileShapeSelect.py

#TYPE IfcFillAreaStyleTileShapeSelect = SELECT
	#(IfcFillAreaStyleTileSymbolWithStyle);
#END_TYPE;

class IfcFillAreaStyleTileShapeSelect(object):
    """"""
    def __init__(self,obj):
        super(IfcFillAreaStyleTileShapeSelect,self).__init__()
        self.lid=obj.lid
        self.m_type=obj.type
        

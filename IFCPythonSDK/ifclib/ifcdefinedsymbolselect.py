#!/usr/bin/python
#coding=utf-8
#Filename:IfcDefinedSymbolSelect.py

#TYPE IfcDefinedSymbolSelect = SELECT
	#(IfcPreDefinedSymbol,IfcExternallyDefinedSymbol);
#END_TYPE;

class IfcDefinedSymbolSelect(object):
    """"""
    def __init__(self,obj):
        super(IfcDefinedSymbolSelect,self).__init__()
        self.lid=obj.lid
        self.m_type=obj.type
        

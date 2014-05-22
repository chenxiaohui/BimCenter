#!/usr/bin/python
#coding=utf-8
#Filename:IfcTextFontSelect.py

#TYPE IfcTextFontSelect = SELECT
	#(IfcPreDefinedTextFont,IfcExternallyDefinedTextFont);
#END_TYPE;

class IfcTextFontSelect(object):
    """"""
    def __init__(self,obj):
        super(IfcTextFontSelect,self).__init__()
        self.lid=obj.lid
        self.m_type=obj.type
        

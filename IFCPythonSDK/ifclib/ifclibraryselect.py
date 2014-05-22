#!/usr/bin/python
#coding=utf-8
#Filename:IfcLibrarySelect.py

#TYPE IfcLibrarySelect = SELECT
	#(IfcLibraryReference,IfcLibraryInformation);
#END_TYPE;

class IfcLibrarySelect(object):
    """"""
    def __init__(self,obj):
        super(IfcLibrarySelect,self).__init__()
        self.lid=obj.lid
        self.m_type=obj.type
        

#!/usr/bin/python
#coding=utf-8
#Filename:IfcDocumentSelect.py

#TYPE IfcDocumentSelect = SELECT
	#(IfcDocumentReference,IfcDocumentInformation);
#END_TYPE;

class IfcDocumentSelect(object):
    """"""
    def __init__(self,obj):
        super(IfcDocumentSelect,self).__init__()
        self.lid=obj.lid
        self.m_type=obj.type
        

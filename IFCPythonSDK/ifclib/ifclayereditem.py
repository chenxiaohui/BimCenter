#!/usr/bin/python
#coding=utf-8
#Filename:IfcLayeredItem.py

#TYPE IfcLayeredItem = SELECT
	#(IfcRepresentationItem,IfcRepresentation);
#END_TYPE;

class IfcLayeredItem(object):
    """"""
    def __init__(self,obj):
        super(IfcLayeredItem,self).__init__()
        self.lid=obj.lid
        self.m_type=obj.type
        

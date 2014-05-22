#!/usr/bin/python
#coding=utf-8
#Filename:IfcClassificationNotationSelect.py

#TYPE IfcClassificationNotationSelect = SELECT
	#(IfcClassificationNotation,IfcClassificationReference);
#END_TYPE;

class IfcClassificationNotationSelect(object):
    """"""
    def __init__(self,obj):
        super(IfcClassificationNotationSelect,self).__init__()
        self.lid=obj.lid
        self.m_type=obj.type
        

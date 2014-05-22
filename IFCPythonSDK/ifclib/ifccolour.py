#!/usr/bin/python
#coding=utf-8
#Filename:IfcColour.py

#TYPE IfcColour = SELECT
	#(IfcColourSpecification,IfcPreDefinedColour);
#END_TYPE;

class IfcColour(object):
    """"""
    def __init__(self,obj):
        super(IfcColour,self).__init__()
        self.lid=obj.lid
        self.m_type=obj.type
        

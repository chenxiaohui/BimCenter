#!/usr/bin/python
#coding=utf-8
#Filename:IfcDraughtingCalloutElement.py

#TYPE IfcDraughtingCalloutElement = SELECT
	#(IfcAnnotationCurveOccurrence,IfcAnnotationTextOccurrence,IfcAnnotationSymbolOccurrence);
#END_TYPE;

class IfcDraughtingCalloutElement(object):
    """"""
    def __init__(self,obj):
        super(IfcDraughtingCalloutElement,self).__init__()
        self.lid=obj.lid
        self.m_type=obj.type
        

#!/usr/bin/python
#coding=utf-8
#Filename:IfcCurveOrEdgeCurve.py

#TYPE IfcCurveOrEdgeCurve = SELECT
	#(IfcBoundedCurve,IfcEdgeCurve);
#END_TYPE;

class IfcCurveOrEdgeCurve(object):
    """"""
    def __init__(self,obj):
        super(IfcCurveOrEdgeCurve,self).__init__()
        self.lid=obj.lid
        self.m_type=obj.type
        

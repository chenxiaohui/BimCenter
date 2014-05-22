#!/usr/bin/python
#coding=utf-8
#Filename:IfcLightDistributionDataSourceSelect.py

#TYPE IfcLightDistributionDataSourceSelect = SELECT
	#(IfcExternalReference,IfcLightIntensityDistribution);
#END_TYPE;

class IfcLightDistributionDataSourceSelect(object):
    """"""
    def __init__(self,obj):
        super(IfcLightDistributionDataSourceSelect,self).__init__()
        self.lid=obj.lid
        self.m_type=obj.type
        

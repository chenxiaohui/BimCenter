#!/usr/bin/python
#coding=utf-8
#Filename:IfcMeasureValue.py

#TYPE IfcMeasureValue = SELECT
	#(IfcVolumeMeasure,IfcTimeMeasure,IfcThermodynamicTemperatureMeasure,IfcSolidAngleMeasure,IfcPositiveRatioMeasure,IfcRatioMeasure,IfcPositivePlaneAngleMeasure,IfcPlaneAngleMeasure,IfcParameterValue,IfcNumericMeasure,IfcMassMeasure,IfcPositiveLengthMeasure,IfcLengthMeasure,IfcElectricCurrentMeasure,IfcDescriptiveMeasure,IfcCountMeasure,IfcContextDependentMeasure,IfcAreaMeasure,IfcAmountOfSubstanceMeasure,IfcLuminousIntensityMeasure,IfcNormalisedRatioMeasure,IfcComplexNumber);
#END_TYPE;

class IfcMeasureValue(object):
    """"""
    def __init__(self,obj):
        super(IfcMeasureValue,self).__init__()
        self.lid=obj.lid
        self.m_type=obj.type
        

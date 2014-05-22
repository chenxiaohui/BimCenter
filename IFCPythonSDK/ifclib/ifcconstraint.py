#!/usr/bin/python
#coding=utf-8
#Filename:IfcConstraint.py
import log
import common
from baseobject import BaseObject
from utils import *

class IFCCONSTRAINT(BaseObject):
    """"""
    def __init__(self,id,arg):
        super(IFCCONSTRAINT,self).__init__(id,arg)
        self.type='IFCCONSTRAINT'
        self.inverse={}
        self.Name=None #IfcLabel
        self.Description=None #IfcText
        self.ConstraintGrade=None #IfcConstraintEnum
        self.ConstraintSource=None #IfcLabel
        self.CreatingActor=None #IfcActorSelect
        self.CreationTime=None #IfcDateTimeSelect
        self.UserDefinedGrade=None #IfcLabel
        self.inverse['Aggregates']=[] #inverse:SET of IfcConstraintAggregationRelationship
        self.inverse['IsRelatedWith']=[] #inverse:SET of IfcConstraintRelationship
        self.inverse['RelatesConstraints']=[] #inverse:SET of IfcConstraintRelationship
        self.inverse['ClassifiedAs']=[] #inverse:SET of IfcConstraintClassificationRelationship
        self.inverse['PropertiesForConstraint']=[] #inverse:SET of IfcPropertyConstraintRelationship
        self.inverse['IsAggregatedIn']=[] #inverse:SET of IfcConstraintAggregationRelationship


    def load(self):
        """register inverses"""
        if not super(IFCCONSTRAINT,self).load():
            return False

        return True

    def init(self):
        """get every argument's value and parse inverses"""
        if not super(IFCCONSTRAINT,self).init():
            return False

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Name= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.Description= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ConstraintGrade= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.ConstraintSource= fromSPF(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.CreatingActor= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.CreationTime= spfToTypeRef(arg)

        arg = self.args.getNext()
        if not isUnset(arg):
            self.UserDefinedGrade= fromSPF(arg)

        inverses = self.args.getInverses('IFCCONSTRAINTAGGREGATIONRELATIONSHIP', 'RelatingConstraint');
        if inverses:
            self.inverse['Aggregates']=inverses

        inverses = self.args.getInverses('IFCCONSTRAINTRELATIONSHIP', 'RelatedConstraints');
        if inverses:
            self.inverse['IsRelatedWith']=inverses

        inverses = self.args.getInverses('IFCCONSTRAINTRELATIONSHIP', 'RelatingConstraint');
        if inverses:
            self.inverse['RelatesConstraints']=inverses

        inverses = self.args.getInverses('IFCCONSTRAINTCLASSIFICATIONRELATIONSHIP', 'ClassifiedConstraint');
        if inverses:
            self.inverse['ClassifiedAs']=inverses

        inverses = self.args.getInverses('IFCPROPERTYCONSTRAINTRELATIONSHIP', 'RelatingConstraint');
        if inverses:
            self.inverse['PropertiesForConstraint']=inverses

        inverses = self.args.getInverses('IFCCONSTRAINTAGGREGATIONRELATIONSHIP', 'RelatedConstraints');
        if inverses:
            self.inverse['IsAggregatedIn']=inverses

        return True

    def getAttrCount(self):
        """get the index of the last attribute"""
        return super(IFCCONSTRAINT,self).getAttrCount()+7

    def toString(self):
        """"""
        line=super(IFCCONSTRAINT,self).toString()       
        line += strToSPF(self.Name)+','
        line += strToSPF(self.Description)+','
        line += typerefToSPF(self.ConstraintGrade)+','
        line += strToSPF(self.ConstraintSource)+','
        line += typerefToSPF(self.CreatingActor)+','
        line += typerefToSPF(self.CreationTime)+','
        line += strToSPF(self.UserDefinedGrade)+','

        return line

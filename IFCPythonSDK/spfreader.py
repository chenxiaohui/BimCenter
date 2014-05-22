#!/usr/bin/python
#coding=utf-8
#Filename:SPFReader.py
from basespfreader import BaseSPFReader
from expressdataset import ExpressDataSet
from spfheader import SPFHeader

class SPFReader(BaseSPFReader):
    """
    self.expressDataSet
    self.header
    """
    def __init__(self):
        super(SPFReader,self).__init__()

    def read(self,fp):
        """ read and parse if file assigned by the fp object
        """
        self.expDataSet=ExpressDataSet()
        self.header=SPFHeader()
        if not BaseSPFReader.read(self,fp):
            return False
        self.expDataSet.setHeader(self.header)


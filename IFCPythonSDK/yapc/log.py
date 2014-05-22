#!/usr/bin/python
#coding=utf-8
#Filename:log.py
import logging
import logging.handlers

def InitLog():
    """"""
    logger=logging.getLogger()
    if logger.handlers:
        return
    hdlr=logging.FileHandler("output.log")
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(logging.NOTSET)

def getLogger():
    """"""
    return logging.getLogger() 

def debug(msg):
    """"""
    getLogger().debug(msg)

def error(msg):
    """"""
    getLogger().error(msg)

def info(msg):
    """"""
    getLogger().info(msg)

def warning(msg):
    """"""
    getLogger().warning(msg)

InitLog()

# Databricks notebook source
def isBinary(s):
    #code here
    myset = set(s)
    print(myset)
    for i in myset:
        if i =='0' or i == '1':
            
            return True
        else:
            return False
        
isBinary("1010101")
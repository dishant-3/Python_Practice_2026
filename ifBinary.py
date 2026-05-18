# Databricks notebook source
def isBinary(s):
    #code here
    myset = set(s)
    print(myset)
    flag = True
    for i in myset:
        if i !='0' or i !='1':
            flag = False
    return flag
        
print(f"Input :1010101 \n Output:{isBinary('1010101')}")
print(f"Input :1020101 \n Output:{isBinary('1020101')}")
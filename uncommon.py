# Databricks notebook source
def uncommonChars(s1,s2):
    set1=set(s1)
    set2=set(s2)
    uncommon=set1.symmetric_difference(set2)
    result=''.join(sorted(uncommon))
    print(result)

s1 = "geeksforgeeks"
s2 = "geeksquiz"
uncommonChars(s1,s2)
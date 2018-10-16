# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 19:46:15 2018

@author: gmous
"""

# =============================================================================
# Counting how many times we get the same string as an original str 
# wehn we moved first char to the last postion in iterated.
# =============================================================================
# =============================================================================
# ORG: ababab
# 1: babab a
# 2: abab ab
# 3: bab aba
# 4: ab abab
# 5: b ababa
# CNT: 2
# =============================================================================

def derek_str(str):
    org_str = str
    new_str = org_str
    cnt = 0
    for i in range(len(org_str)-1):
        new_str = new_str[1:] + new_str[0]
        if new_str == org_str:
            cnt += 1
            print("Same! %s" %new_str)
        else: 
            print("Different! %s" %new_str)
    print("=========== Total Count: %i" %cnt)

derek_str("abababab")

# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 19:46:15 2018

@author: gmous
"""
# =============================================================================
# Sorting the array by Alphabet
# If there is a string only having same char such as bbb and bbbb,
# it should be sorted by length
# =============================================================================
# =============================================================================
# <INPUT>
# zre
# asf
# bbbbbbbbbbb
# bb
# bbbbb
# tgb
# 
# <OUTPUT>
# asf
# bbbbbbbbbbb
# bbbbb
# bb
# tgb
# zre
# =============================================================================

str = ["zre", "asf", "bbbbbbb", "bbbb", "babbb", "aab", "baa", "tgb"]

# Compared Average Ascii code
def compare_ascii(str1, str2):
    str1_ascii = sum(map(ord, str1))/len(str1)
    str2_ascii = sum(map(ord, str2))/len(str2)
    
    if str1_ascii == str2_ascii:
        return True
    else:
        return False

# Solted by Alphabet
b = list(sorted(str))

# Check Same Char used
# if there is, swap it
for i in range(len(b)-1):
    if compare_ascii(b[i], b[i+1]):
        print("Prev List: ", b)
        if len(b[i]) < len(b[i+1]):
            b[i], b[i+1] = b[i+1], b[i]
            print("Changed List: ", b)
print("Result: ", b)

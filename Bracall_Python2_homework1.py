# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 14:00:09 2020

@author: kayla.bracall
DAT 129
Homework 1
"""
# add pattern to lists
list_a = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
list_b = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
list_c = [1, 0, 1, 0, 0, 0, 0, 0, 0, 0]
list_d = [0, 1, 0, 1, 0, 1, 1, 1, 0, 0]
list_e = [0, 0, 1, 0, 1, 0, 0, 0, 1, 0]
list_f = [0, 0, 0, 1, 0, 0, 0, 0, 0, 1]
list_g = [0, 0, 0, 1, 0, 0, 0, 0, 0, 1]
list_h = [0, 0, 0, 1, 0, 0, 0, 0, 0, 1]
list_i = [0, 0, 0, 0, 1, 0, 0, 0, 1, 0]
list_j = [0, 0, 0, 0, 0, 1, 1, 1, 0, 1]

# define function that will print lists
def list_printer(list):
    for item in range(len(list)):
        if item == 1:
            print('*', end = '')
        elif item == 0:
            print('x', end = '')

def main():
# call function for each list             
    list_printer(list_a)
    list_printer(list_b)
    list_printer(list_c)
    list_printer(list_d)
    list_printer(list_e)
    list_printer(list_f)
    list_printer(list_g)
    list_printer(list_h)
    list_printer(list_i)
    list_printer(list_j)
    
main()



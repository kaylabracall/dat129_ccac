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
    for item in (list):
        # one is "on"
        if item == 1:
            print('X', end = '')
        # zero is "off"
        elif item == 0:
            print('*', end = '')
    print(end = '\n')
# pull lists into master list so that list_printer only has to be called once  
list_master = [list_a, list_b, list_c, list_d, list_e, list_f, list_g, list_h, 
               list_i, list_j]


def master_list_printer(master_list):
    for list in master_list:
        list_printer(list)
        
def main():
# call function for each list             
    master_list_printer(list_master)
    
    
main()




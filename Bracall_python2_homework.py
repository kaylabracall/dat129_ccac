# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 20:46:56 2020

@author: kaybr
"""

import csv

def process_capital_projects():
    ''' this function iterates over the capital_projects csv file to determine
    percentage of completed projects'''
    
    file = open('capital_projects.csv', newline= '')
    reader = csv.DictReader(file)
    status_count = {'Planned':0, 'Completed':0, 'In_Progress':0, 'Canceled':0}
    #comp_status = 'Completed'
    #plan_status = 'Planned'
    #in_prog_status = 'In_Progress'
    #cancel_status = 'Canceled'
    
    for row in reader:
        if row['status'] == 'Planned':
            status_count['Planned'] = status_count['Planned'] +1
        elif row['status'] == 'Completed':
            status_count['Completed'] = status_count['Completed'] +1
        elif row['status'] == 'In_Progress':
            status_count['In_Progress'] = status_count['In_Progress'] +1
        elif row['status'] == 'Canceled':
            status_count['Canceled'] = status_count['Canceled'] +1
        else:
            print ('This should not print')
    return status_count

process_capital_projects()

def compute_percentage(status_count):
    total = 0
    
    for item in status_count:
        total = total + status_count[item]
        
        
        
        
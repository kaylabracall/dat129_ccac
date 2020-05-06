# -*- coding: utf-8 -*-
"""
Created on Tue May  5 18:28:42 2020

@author: kaybr
"""

import csv
import urllib
from bs4 import BeautifulSoup
# getting html from search results at ravelery.com for both knitting and crochet patterns

def get_search_url(term):
    '''assembles a query against goodreads.com given a search term'''
    url = "https://www.yarn.com/search?&q=%s" % (str(term))
    return url

def getPageText(url):
    '''Given a URL, fetches the raw HTML''' 
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        return response.read()

def get_user_input():
    yarn_list = ['silk', 'wool', 'polyester', 'bamboo', 'cotton', 'cashmere', 'luxury']
    for item in yarn_list:
        print(item, sep='')
    search_term = input('Please enter a yarn type from list: ')
    if search_term not in yarn_list:
        print('That is not a yarn type, please try again.')
        input('Please enter a yarn from list: ')
    return search_term



def scrape_function(): 
    term = str(get_user_input())
    pageText = getPageText(get_search_url(term))
    soup = BeautifulSoup(pageText, 'html.parser')
    s = soup.find_all('div','product-prices__price')
    count = 0
    tot_price = 0


    for item in s:
        price = item.find('span', None)
        if price:
            count = count +1 # increase counter
            price_variable = price.text
            price_num = float(price_variable.replace('$','')) # cast to float and replace the $ with an empty string
            tot_price = tot_price + price_num
        else:
            continue

    #print(str(tot_price))
    #print(wool_count)

    wool_average_price = float(tot_price)/count
    pretty_count = round(wool_average_price, 2)
    
    yarn_dictionary = {}
    if term == 'silk':
        yarn_dictionary['silk'] = pretty_count
    elif term == 'wool':
        yarn_dictionary['wool'] = pretty_count
    elif term == 'polyester':
        yarn_dictionary['polyester'] = pretty_count
    elif term == 'bamboo':
        yarn_dictionary['bamboo']= pretty_count
    elif term == 'cotton':
        yarn_dictionary['cotton']= pretty_count
    elif term == 'cashmere':
        yarn_dictionary['cashmere'] = pretty_count
    elif term == 'luxury':
        yarn_dictionary['luxury'] = pretty_count
        
            
    return(yarn_dictionary)
    #print(pretty_wool)
    
yarn_dict = scrape_function()

    
with open('yarndict.csv', 'w') as y:
    fnames = ['silk', 'wool', 'polyester', 'bamboo', 'cashmere', 'cotton', 'luxury']
    writer = csv.DictWriter(y, fieldnames= fnames)
    writer.writeheader()
    writer.writerow(yarn_dict)
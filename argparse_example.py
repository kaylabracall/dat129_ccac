# -*- coding: utf-8 -*-
"""
Created on Sun May  3 18:56:11 2020

@author: kaybr
"""

import argparse

def parse_argument():
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--player', choices=['mickey_mantle','babe_ruth','lou_gehrig'], help = 'Name of the player')
    args = parser.parse_args()
    player = args.player
    
def retrieve_stats(player):
    babe_ruth = {'BA':.342, 'RBIs': 2213, 'GP': 2503}
    mickey_matle = {'BA': .298, "RBIs": 1509, "GP" : 2401}
    lou_gehrig =  {'BA': .340, "RBIs": 1995, "GP":21604}
    if player == 'babe_ruth':
        return babe_ruth
    elif player == 'mickey_mantle':
        return mickey_matle
    elif player == 'lou_gehrig': 
        return lou_gehrig
    
def pretty_print(player_stats):
    print(str(player_stats['BA']))
    print(str(player_stats['RBIs']))
    print(str(player_stats['GP']))
    
def main():
    player = parse_argument
    player_stats = retrieve_stats(player)
    pretty_print(player_stats)
    
if __name__ == "__main__":
    main()
    
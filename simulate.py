#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# File Name: simulate.py
# Created By: Hernan Mogliasso
# Created Date: March 31th 2022
# Description: Simulation of the 2022 world cup draw
# =============================================================================

import random
import numpy as np

# Static values

NUMBER_OF_GROUPS = 8
TEAMS_PER_GROUP = 4

pot_1 = ['Qatar', 'Belgium', 'Brasil', 'France', 'Argentina', 'England', 'Spain', 'Portugal']
pot_2 = ['Denmark', 'Netherlands', 'Germany', 'Mexico', 'United States', 'Switzerland', 'Croatia', 'Uruguay']
pot_3 = ['Senegal', 'Iran', 'Japan', 'Morocco', 'Serbia', 'Poland', 'South Corea', 'Canada']
pot_4 = ['Ecuador', 'Saudi Arabia', 'Ghana', 'Tunisia', 'Cameroon' , 'CONMEBOL - AFC Playoff', 'CONCACAF - OFC Playoff', 'UEFA Playoff']
groups = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

LOCAL_TEAM = 'Qatar'

def take_ball(pot):
    """Simulates picking up a ball from the pot. 
       Returns None if the pot is empty.
    """
    ball = None
    if len(pot) > 0: 
        random.shuffle(pot)
        ball = random.sample(pot, k=1)[0]
        pot.remove(ball)
    return ball

def simulate_draw():
    """Simulates the whole draw"""
    team_pots = [pot_1.copy(), pot_2.copy(), pot_3.copy(), pot_4.copy()]
    group_pots = { l: [n for n in range(TEAMS_PER_GROUP)] for l in groups}

    draw_result = np.empty([8,4], dtype=np.object_) # to store the results in a np array
    for i, p in enumerate(team_pots):
        j = 0
        while p: 
            if i==0 and j==0: # first time
                draw_result[0][0] = LOCAL_TEAM
                p.remove(LOCAL_TEAM)
                group_pots['A'].remove(0)
            else:
                team_ball = take_ball(p)
                curr_group = groups[j]
                group_ball = take_ball(group_pots[curr_group])
                draw_result[j][group_ball] = team_ball
            j +=1
    return draw_result

if __name__=='__main__':
    draw = simulate_draw()    
    for g, s in zip(groups, draw):
        print(f"Group {g}:    {s[0]:<23s} {s[1]:<23s} {s[2]:<23s} {s[3]:<23s}")